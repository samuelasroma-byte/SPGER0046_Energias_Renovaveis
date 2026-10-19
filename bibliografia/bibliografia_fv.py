"""Reproducible theoretical reading survey, not novelty detection.

Provider citations remain separate. Credentials are read in memory only.
Cached responses never include request URLs, request headers or API keys.
"""
from pathlib import Path
from datetime import datetime, timezone
from difflib import SequenceMatcher
from concurrent.futures import ThreadPoolExecutor
import hashlib,html,json,os,re,time,unicodedata
import requests
import pandas as pd
import formatacao_abnt as abnt

SOURCES=['OpenAlex','Crossref','Scopus','WOS','IEEE Xplore']
ENDPOINTS={'OpenAlex':'https://api.openalex.org/works',
 'Crossref':'https://api.crossref.org/works',
 'Scopus':'https://api.elsevier.com/content/search/scopus',
 'WOS':'https://api.clarivate.com/apis/wos-starter/v1/documents',
 'IEEE Xplore':'https://ieeexploreapi.ieee.org/api/v1/search/articles'}
SECRET_NAMES={'OpenAlex':'OPENALEX_API_KEY','Scopus':'SCOPUS_API_KEY','WOS':'WOS_API_KEY','IEEE Xplore':'IEEE_API_KEY'}
TITLE_GATES={
 '1.1':[['solar position','solar geometry','sun position','solar zenith']],
 '1.2':[['solar irradiance','solar radiation'],['global','direct','diffuse','component','radiometr']],
 '1.3':[['irradiance','solar radiation','surface solar'],['variab','cloud','aerosol','atmospher','turbidity']],
 '1.4':[['solar radiation','solar resource','solar irradiance'],['measur','quality','uncertainty','monitor','validat']],
 '2.1':[['temperature','thermal'],['photovoltaic','pv module','solar module','solar panel']],
 '2.2':[['albedo','reflectance']],
 '2.3':[['soiling','dust','shading'],['photovoltaic','solar','pv ']],
 '2.4':[['tilt','orientation','azimuth'],['photovoltaic','pv ','solar']],
 '3.1':[['transposition','tilted','plane of array'],['irradiance','radiation','solar']],
 '3.2':[['temperature','thermal'],['photovoltaic','pv module','solar module','solar panel']],
 '3.3':[['diode','equivalent circuit'],['photovoltaic','solar cell']],
 '3.4':[['array','interconnection','mismatch'],['photovoltaic','pv ']],
 '3.5':[['inverter']],
 '3.6':[['energy yield','energy prediction','performance model'],['photovoltaic','pv ']],
 '4.1':[['loss','degradation'],['photovoltaic','pv ','solar module']],
 '4.2':[['specific yield','final yield','reference yield','performance parameter']],
 '4.3':[['performance ratio']],
 '4.4':[['validat','error','metric','blind','benchmark','model compar'],['photovoltaic','solar power','pv ']],
 '4.5':[['building integrated','bipv','facade','glazing','solar window']],
}

def clean(x):
    return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',str(x or '')))).strip()

def norm(x):
    return re.sub('[^a-z0-9]+',' ',unicodedata.normalize('NFKD',clean(x)).encode('ascii','ignore').decode().lower()).strip()

def doi(x):
    return re.sub(r'^(https?://(dx\.)?doi.org/|doi:\s*)','',str(x or '').strip(),flags=re.I).lower()

def secret(name):
    value=os.environ.get(name,'').strip()
    if value:return value
    try:
        from google.colab import userdata
        return str(userdata.get(name) or '').strip()
    except Exception:return ''

def abstract_openalex(inv):
    if not inv:return ''
    ordered={position:word for word,positions in inv.items() for position in positions}
    return ' '.join(ordered[i] for i in sorted(ordered))

def year_crossref(w):
    for field in ['published-print','published-online','published','issued']:
        dates=(w.get(field) or {}).get('date-parts') or []
        if dates and dates[0]:return dates[0][0]
    return None

def record(source,w,topic,fetched):
    r=dict(source=source,query_topic=topic,retrieved_at=fetched,doi='',title='',authors='',year=None,
       venue='',document_type='',citation_count=None,record_id='',url='',oa_url='',oa_status='',isbn='',
       abstract='',volume='',issue='',pages='',publisher='',edition='',issn='',
       seed_ids=[],seed_topics=[],seed_roles=[],seed_priority=0)
    if source=='OpenAlex':
        location=w.get('primary_location') or {};src=location.get('source') or {};oa=w.get('open_access') or {}
        r.update(doi=doi(w.get('doi')),title=w.get('display_name') or w.get('title',''),year=w.get('publication_year'),
          authors='; '.join((a.get('author') or {}).get('display_name','') for a in w.get('authorships',[])),
          venue=src.get('display_name',''),document_type=w.get('type',''),citation_count=w.get('cited_by_count'),
          record_id=w.get('id',''),url=location.get('landing_page_url') or w.get('doi') or w.get('id',''),
          oa_url=oa.get('oa_url') or '',oa_status=oa.get('oa_status') or '',abstract=abstract_openalex(w.get('abstract_inverted_index')))
        b=w.get('biblio') or {}
        r.update(volume=b.get('volume') or '',issue=b.get('issue') or '',issn=src.get('issn_l') or '',
                 pages='–'.join(str(x) for x in [b.get('first_page'),b.get('last_page')] if x))
    elif source=='Crossref':
        fulltitle=(w.get('title') or [''])[0]
        if w.get('subtitle'):fulltitle+=': '+w['subtitle'][0]
        r.update(doi=doi(w.get('DOI')),title=fulltitle,year=year_crossref(w),
          authors='; '.join(' '.join([a.get('given',''),a.get('family','')]).strip() for a in (w.get('author') or w.get('editor') or [])),
          venue=(w.get('container-title') or [''])[0] or w.get('publisher',''),document_type=w.get('type',''),
          citation_count=w.get('is-referenced-by-count'),record_id=doi(w.get('DOI')),url=w.get('URL',''),
          isbn='; '.join(w.get('ISBN') or []),abstract=clean(w.get('abstract','')))
        r.update(volume=w.get('volume') or '',issue=w.get('issue') or '',pages=w.get('page') or w.get('article-number') or '',
                 publisher=w.get('publisher') or '',edition=w.get('edition-number') or '',issn='; '.join(w.get('ISSN') or []))
    elif source=='Scopus':
        r.update(doi=doi(w.get('prism:doi')),title=w.get('dc:title',''),year=str(w.get('prism:coverDate',''))[:4] or None,
          authors=w.get('dc:creator',''),venue=w.get('prism:publicationName',''),document_type=w.get('subtypeDescription',''),
          citation_count=w.get('citedby-count'),record_id=w.get('eid',''),url=next((x.get('@href','') for x in w.get('link',[]) if x.get('@ref')=='scopus'),''),
          abstract=w.get('dc:description',''))
    elif source=='WOS':
        ids=w.get('identifiers') or {};src=w.get('source') or {}
        r.update(doi=doi(ids.get('doi')),title=w.get('title',''),year=src.get('publishYear'),
          authors='; '.join(a.get('displayName','') for a in (w.get('names') or {}).get('authors',[])),
          venue=src.get('sourceTitle',''),document_type='; '.join(w.get('types') or []),record_id=w.get('uid',''),
          citation_count=next((c.get('count') for c in w.get('citations',[]) if c.get('db')=='WOS'),None),
          url=(w.get('links') or {}).get('record',''))
    elif source=='IEEE Xplore':
        r.update(doi=doi(w.get('doi')),title=w.get('title',''),year=w.get('publication_year'),
          authors='; '.join(a.get('full_name','') for a in (w.get('authors') or {}).get('authors',[])),
          venue=w.get('publication_title',''),document_type=w.get('content_type',''),citation_count=w.get('citing_paper_count'),
          record_id=str(w.get('article_number','')),url=w.get('html_url',''),abstract=w.get('abstract',''))
    for field in ['title','authors','venue','abstract']:r[field]=clean(r[field])
    r['authors']='; '.join(a.strip() for a in r['authors'].replace(' (Deceased)','').split(';') if a.strip())
    try:r['year']=int(r['year']) if r['year'] else None
    except (ValueError,TypeError):r['year']=None
    try:r['citation_count']=int(r['citation_count']) if r['citation_count'] is not None else None
    except (ValueError,TypeError):r['citation_count']=None
    return r

class Survey:
    def __init__(self,root,live=True):
        self.root=Path(root);self.cfg=json.loads((self.root/'protocolo.json').read_text())
        self.topics=json.loads((self.root/'temas.json').read_text());self.seeds=json.loads((self.root/'sementes.json').read_text())
        self.live=live;self.keys={s:secret(n) for s,n in SECRET_NAMES.items()};self.logs=[]
        self.raw=self.root/'raw';self.out=self.root/'outputs'
        for p in [self.raw,self.out,self.out/'por_secao',self.out/'logs']:p.mkdir(parents=True,exist_ok=True)

    def get(self,source,label,params=None,headers=None,suffix=''):
        cache=self.raw/(re.sub('[^A-Za-z0-9_.-]','_',source+'_'+label)+'.json')
        if cache.exists():
            envelope=json.loads(cache.read_text())
            self.logs.append(dict(source=source,query=label,status='cache',http=200,retrieved_at=envelope['retrieved_at']))
            return envelope['data'],envelope['retrieved_at']
        if not self.live:
            self.logs.append(dict(source=source,query=label,status='cache ausente; rede desativada',http=None))
            return None,None
        for attempt in range(self.cfg['maximum_attempts']):
            try:
                response=requests.get(ENDPOINTS[source]+suffix,params=params,headers=headers,timeout=self.cfg['request_timeout_seconds'])
                status=response.status_code
                if status==200:
                    data=response.json();stamp=datetime.now(timezone.utc).isoformat()
                    # Deliberately store the response only, without credential-bearing request data.
                    cache.write_text(json.dumps({'retrieved_at':stamp,'source':source,'query':label,'data':data},ensure_ascii=False))
                    self.logs.append(dict(source=source,query=label,status='coletado',http=status,retrieved_at=stamp))
                    return data,stamp
                if status not in [429,500,502,503,504]:break
            except (requests.RequestException,ValueError) as exc:
                status=type(exc).__name__
            if attempt+1<self.cfg['maximum_attempts']:time.sleep(min(2**attempt,4))
        self.logs.append(dict(source=source,query=label,status='falha registrada',http=status))
        return None,None

    def query(self,topic,source,mode='citados'):
        query=topic['query'];label=topic['id'].replace('.','_')+'_'+('recentes_citados' if mode=='recentes' else mode)
        key=self.keys.get(source,'');limit=self.cfg['institutional_per_query']
        if source in ['Scopus','WOS','IEEE Xplore'] and not key:return []
        if source=='OpenAlex':
            fil=f'from_publication_date:{self.cfg["from_year"]}-01-01,to_publication_date:{self.cfg["through_date"]},is_retracted:false'
            if mode=='recentes':fil=f'from_publication_date:{self.cfg["recent_from_year"]}-01-01,to_publication_date:{self.cfg["through_date"]},is_retracted:false'
            params={'search':query,'filter':fil,'per-page':self.cfg['openalex_recent_per_query' if mode=='recentes' else 'openalex_per_query'],
                    'sort':'cited_by_count:desc'}
            if key:params['api_key']=key
            data,stamp=self.get(source,label,params);items=(data or {}).get('results',[])
        elif source=='Crossref':
            params={'query.bibliographic':query,'rows':self.cfg['crossref_per_query'],
                    'filter':f'from-pub-date:{self.cfg["from_year"]}-01-01,until-pub-date:{self.cfg["through_date"]}'}
            data,stamp=self.get(source,label,params);items=((data or {}).get('message') or {}).get('items',[])
        elif source=='Scopus':
            expression=' AND '.join('"'+v+'"' for v in query.split() if len(v)>2)
            params={'query':'TITLE-ABS-KEY('+expression+')','count':min(25,limit),'start':0,'view':'STANDARD'}
            data,stamp=self.get(source,label,params,{'X-ELS-APIKey':key,'Accept':'application/json'})
            items=((data or {}).get('search-results') or {}).get('entry',[])
        elif source=='WOS':
            params={'db':'WOS','q':'TS=('+ ' AND '.join(query.split())+')','limit':min(50,limit),'page':1}
            data,stamp=self.get(source,label,params,{'X-ApiKey':key});items=(data or {}).get('hits',[])
        else:
            params={'apikey':key,'querytext':query,'max_records':min(200,limit),'start_record':1,
                    'start_year':self.cfg['from_year'],'end_year':int(self.cfg['through_date'][:4])}
            data,stamp=self.get(source,label,params);items=(data or {}).get('articles',[])
        return [record(source,w,topic['id'],stamp) for w in items if w]

    def seed_records(self):
        records=[];resolution=[]
        for seed in self.seeds:
            d=seed.get('doi') or '';found=[];state='fonte técnica indicada; sem contagem bibliométrica'
            if d:
                data,stamp=self.get('Crossref','doi_'+hashlib.sha1(d.encode()).hexdigest()[:14],suffix='/'+d)
                if data:
                    rr=record('Crossref',data['message'],'semente',stamp)
                    if SequenceMatcher(None,norm(seed['title']),norm(rr['title'])).ratio()>=.56:found.append(rr);state='DOI e título conferidos no Crossref'
                params={}
                if self.keys.get('OpenAlex'):params['api_key']=self.keys['OpenAlex']
                data,stamp=self.get('OpenAlex','doi_'+hashlib.sha1(d.encode()).hexdigest()[:14],params=params,suffix='/https://doi.org/'+d)
                if data:
                    rr=record('OpenAlex',data,'semente',stamp)
                    if SequenceMatcher(None,norm(seed['title']),norm(rr['title'])).ratio()>=.56:found.append(rr);state='DOI e título conferidos em índice bibliográfico'
            elif seed.get('verify_by_title'):
                data,stamp=self.get('Crossref','title_'+seed['seed_id'],{'query.bibliographic':seed['title'],'rows':5})
                candidates=[record('Crossref',w,'semente',stamp) for w in ((data or {}).get('message') or {}).get('items',[])]
                candidates.sort(key=lambda r:SequenceMatcher(None,norm(seed['title']),norm(r['title'])).ratio(),reverse=True)
                if candidates and SequenceMatcher(None,norm(seed['title']),norm(candidates[0]['title'])).ratio()>=.76:
                    found=[candidates[0]];state='título e DOI localizados no Crossref'
            if not found:
                if seed.get('verify_by_title'):
                    resolution.append(dict(seed_id=seed['seed_id'],title=seed['title'],status='não resolvida automaticamente; excluída da seleção'))
                    continue
                found=[dict(record('Crossref',{},'semente',None),source='Curadoria',title=seed['title'],authors=seed['authors'],
                   year=seed['year'] if isinstance(seed['year'],int) else None,doi=d,url=seed['url'],document_type=seed['kind'],
                   citation_count=None,record_id=seed['seed_id'])]
                if d:state='DOI da fonte original preservado; índice indisponível'
            for rr in found:
                rr.update(seed_ids=[seed['seed_id']],seed_topics=seed['topics'],seed_roles=[seed['role']],seed_priority=seed['priority'])
                if not rr['authors'] and seed['authors']:
                    rr['authors']=seed['authors'];rr['authorship_source']=seed.get('authorship_source') or seed['url']
                if seed['seed_id']=='S03':
                    rr['title']='Solar Energy Engineering: Processes and Systems';rr['edition']='2'
                if rr['year'] is None and isinstance(seed['year'],int):rr['year']=seed['year']
                if seed['seed_id']=='S02':
                    rr['indexed_year']=rr['year'];rr['year']=2011
                    rr['year_note']='Edição impressa com copyright 2011; lançamento eletrônico indexado em dezembro de 2010.'
                    rr['indexed_edition']=rr.get('edition');rr['edition']='2'
                    rr['edition_source']='https://onlinelibrary.wiley.com/doi/10.1002/9780470974704.fmatter'
                    rr['contributors_role']='editors'
                if seed['kind']=='livro':rr['document_type']='livro'
                records.append(rr)
            resolution.append(dict(seed_id=seed['seed_id'],title=found[0]['title'],doi=found[0]['doi'],status=state))
        pd.DataFrame(resolution).to_csv(self.out/'logs/resolucao_sementes.csv',index=False)
        return records

    def collect(self):
        availability=[]
        for source in SOURCES:
            available=source not in ['Scopus','WOS','IEEE Xplore'] or bool(self.keys.get(source))
            availability.append(dict(base=source,status='habilitada' if available else 'não consultada; credenciais não disponíveis na coleta registrada',
                credencial_presente=bool(self.keys.get(source)) if source!='Crossref' else 'não exigida'))
        self.availability=pd.DataFrame(availability);self.availability.to_csv(self.out/'logs/estado_bases.csv',index=False)
        tasks=[(t,s,m) for t in self.topics for s in SOURCES for m in (['citados','recentes'] if s=='OpenAlex' else ['relevancia'])
               if s in ['OpenAlex','Crossref'] or self.keys.get(s)]
        records=[]
        # Independent public searches, bounded at three simultaneous requests.
        with ThreadPoolExecutor(max_workers=3) as pool:
            for result in pool.map(lambda args:self.query(*args),tasks):records.extend(result)
        records.extend(self.seed_records())
        self.records=records
        (self.out/'registros_normalizados.json').write_text(json.dumps(records,ensure_ascii=False,indent=2))
        pd.DataFrame(self.logs).to_csv(self.out/'logs/consultas_executadas.csv',index=False)
        return records

    def consolidate(self):
        groups={}
        for rr in self.records:
            if not rr['title']:continue
            key='doi:'+rr['doi'] if rr['doi'] else 'title:'+norm(rr['title'])+'|'+str(rr['year'])
            group=groups.setdefault(key,[]);group.append(rr)
        works=[]
        for key,items in groups.items():
            preferred=sorted(items,key=lambda r:(r['source']=='Crossref',bool(r['authors']),len(r['title'])),reverse=True)[0]
            w={k:preferred.get(k) for k in ['doi','title','authors','year','venue','document_type','url','isbn',
                                          'volume','issue','pages','publisher','edition','issn']}
            for field in list(w):
                if w[field] in [None,'']:w[field]=next((r.get(field) for r in items if r.get(field) not in [None,'']),w[field])
            note=next((r.get('year_note') for r in items if r.get('year_note')),'')
            if note:
                w['indexed_year']=next(r.get('indexed_year') for r in items if r.get('year_note'))
                w['year_note']=note;w['year']=2011
            if any(r.get('edition_source') for r in items):
                corrected=next(r for r in items if r.get('edition_source'))
                for field in ['edition','indexed_edition','edition_source','contributors_role']:w[field]=corrected.get(field)
            if any(r.get('authorship_source') for r in items):
                w['authorship_source']=next(r['authorship_source'] for r in items if r.get('authorship_source'))
            w['id']='FV'+hashlib.sha1(key.encode()).hexdigest()[:9]
            w['query_topics']=sorted(set(r['query_topic'] for r in items if r['query_topic']!='semente'))
            for key2 in ['seed_ids','seed_topics','seed_roles']:w[key2]=sorted(set(v for r in items for v in r[key2]))
            w['seed_priority']=max(r['seed_priority'] for r in items)
            w['sources']=sorted(set(r['source'] for r in items))
            w['abstract']=max((r['abstract'] for r in items),key=len)
            w['oa_url']=next((r['oa_url'] for r in items if r['oa_url']),'')
            w['oa_status']=next((r['oa_status'] for r in items if r['oa_status']),'não informado')
            for source in SOURCES:
                arr=[r for r in items if r['source']==source and r['citation_count'] is not None]
                # A provider's most recently retrieved observation, never a sum across databases.
                arr.sort(key=lambda r:r['retrieved_at'] or '',reverse=True)
                w['citations_'+source]=arr[0]['citation_count'] if arr else None
                w['citations_date_'+source]=arr[0]['retrieved_at'] if arr else None
                w['record_id_'+source]=arr[0]['record_id'] if arr else None
            if any(r['document_type']=='livro' for r in items):w['document_type']='livro'
            w['reading_status']='metadados e resumo quando disponível; leitura integral pendente'
            works.append(w)
        self.works=works
        self.enrich_openalex()
        return self.works

    def enrich_openalex(self):
        # Verified seed DOIs and the strongest candidates can receive missing citation metadata.
        eligible=[w for w in self.works if w['doi'] and w['citations_OpenAlex'] is None and w['seed_ids']]
        for w in eligible:
            data,stamp=self.get('OpenAlex','doi_'+hashlib.sha1(w['doi'].encode()).hexdigest()[:14],
                 {'api_key':self.keys['OpenAlex']} if self.keys.get('OpenAlex') else {},suffix='/https://doi.org/'+w['doi'])
            if not data:continue
            if SequenceMatcher(None,norm(w['title']),norm(data.get('display_name',''))).ratio()<.60:continue
            w.update(citations_OpenAlex=data.get('cited_by_count'),citations_date_OpenAlex=stamp,record_id_OpenAlex=data.get('id'))
            w['oa_url']=(data.get('open_access') or {}).get('oa_url') or w['oa_url']
            w['sources']=sorted(set(w['sources']+['OpenAlex']))
        pd.DataFrame(self.logs).to_csv(self.out/'logs/consultas_executadas.csv',index=False)

    def relevance(self,w,topic):
        if topic['id'] in w['seed_topics']:return 1.0,'obra de base ou método indicado para este tópico'
        text=norm(w['title']+' '+w['abstract']);title=norm(w['title'])
        if any(x in title for x in ['solar dynamics observatory','solar cycle','solar flare','coronal','sunspot']):
            return 0.0,'física solar fora do recurso solar terrestre deste capítulo'
        if w['document_type'] in ['dissertation','posted-content','grant','peer-review','dataset']:
            return 0.0,'tipo documental fora da seleção automática de fundamentação'
        if not all(any(norm(term) in title for term in group) for group in TITLE_GATES[topic['id']]):
            return 0.0,'título sem correspondência específica com o tópico'
        if topic['id'] in ['2.1','3.2','4.1'] and any(x in title for x in ['perovskite','organic','polymer']) and not any(x in title for x in ['module','system','panel']):
            return 0.0,'materiais de célula fora da modelagem do sistema instalado'
        matches=[term for term in topic['relevance_terms'] if norm(term) in text]
        title_matches=[term for term in topic['relevance_terms'] if norm(term) in title]
        solar=any(v in text for v in ['photovoltaic','irradiance','solar radiation','solar energy','solar position'])
        if not solar:return 0.0,'fora do domínio solar explícito'
        score=min(.95,.30*len(matches)+.25*bool(title_matches))
        return score,'termos identificados: '+', '.join(matches)

    def select(self):
        links=[];chosen=[];topcited=[];recent=[]
        for topic in self.topics:
            candidates=[]
            for w in self.works:
                if topic['id'] not in w['query_topics']+w['seed_topics']:continue
                score,reason=self.relevance(w,topic)
                if score<.5:continue
                link=dict(w,topic=topic['id'],topic_title=topic['title'],owner=topic['owner'],relevance=score,match_reason=reason)
                candidates.append(link);links.append(link)
            cite=lambda w:w['citations_OpenAlex'] if w['citations_OpenAlex'] is not None else -1
            cited=sorted([w for w in candidates if w['citations_OpenAlex'] is not None],key=cite,reverse=True)
            topcited.extend(dict(w,rank_in_retrieved_topic=i) for i,w in enumerate(cited[:10],1))
            newest=sorted([w for w in candidates if w['year'] and w['year']>=self.cfg['recent_from_year']
                and (w['seed_ids'] or (w['citations_OpenAlex'] is not None and w['citations_OpenAlex']>=10))],
                key=lambda w:(cite(w),w['year']),reverse=True)
            recent.extend(newest[:5])
            seeds=sorted([w for w in candidates if topic['id'] in w['seed_topics']],
                         key=lambda w:(w['seed_priority'],cite(w)),reverse=True)
            # Keep a book, topic-specific methods, a frequently cited candidate and a recent candidate.
            selected=[]
            def add(w,role):
                if w and w['id'] not in [x['id'] for x in selected]:selected.append(dict(w,selection_role=role))
            books=[w for w in seeds if w['document_type']=='livro']
            if books:add(books[0],'livro de base')
            for w in [s for s in seeds if s['document_type']!='livro'][:3]:add(w,'método ou fonte técnica do tópico')
            if cited:add(cited[0],'elevada citação no conjunto recuperado')
            if newest:add(newest[0],'complemento recente no recorte consultado')
            for w in seeds+cited:
                if len(selected)>=6:break
                add(w,'leitura complementar')
            chosen.extend(selected)
        self.links=links;self.selected=chosen;self.topcited=topcited;self.recent=recent
        assert set(w['topic'] for w in chosen)==set(t['id'] for t in self.topics),'Tópico sem leituras efetivas'
        return chosen

    def export(self):
        unique_priority={w['id']:w for w in self.selected}
        labels={w['id']:f'B{i:02d}' for i,w in enumerate(sorted(unique_priority.values(),key=abnt.sort_key),1)}
        for rows in [self.works,self.links,self.selected,self.topcited,self.recent]:
            for w in rows:w['reference_code']=labels.get(w['id'],'')
        def flatten(rows):
            result=[]
            for w in rows:
                row={k:('; '.join(str(v) for v in value) if isinstance(value,list) else value) for k,value in w.items() if k!='abstract'}
                row['reference']=citation(w);result.append(row)
            return pd.DataFrame(result)
        self.catalog=flatten(self.works);self.reading=flatten(self.selected)
        for name,rows in [('catalogo_consolidado',self.works),('catalogo_por_subsecao',self.links),
                         ('obras_prioritarias',self.selected),('top_citados_por_subsecao',self.topcited),('complementos_recentes',self.recent)]:
            flatten(rows).to_csv(self.out/(name+'.csv'),index=False)
        (self.out/'catalogo_completo.json').write_text(json.dumps(self.works,ensure_ascii=False,indent=2))
        (self.out/'leituras_prioritarias.json').write_text(json.dumps(self.selected,ensure_ascii=False,indent=2))
        bibliography=[];ris=[]
        unique={w['id']:w for w in self.selected}
        for w in unique.values():
            safe=lambda text:str(text or '').replace('{','').replace('}','')
            kind='book' if w['document_type']=='livro' else 'techreport' if 'report' in str(w['document_type']) else 'inproceedings' if 'proceeding' in str(w['document_type']).lower() else 'article' if w['doi'] else 'misc'
            bibliography.append('@'+kind+'{'+w['id']+',\n'+',\n'.join('  '+k+' = {'+safe(v)+'}' for k,v in
               [('title',w['title']),('editor' if w.get('contributors_role')=='editors' else 'author',str(w['authors']).replace('; ',' and ')),('year',w['year']),('doi',w['doi']),('url',w['url']),
                ('publisher' if kind=='book' else 'institution' if kind=='techreport' else 'booktitle' if kind=='inproceedings' else 'journal',w['venue']),
                ('edition',w.get('edition')),('volume',w.get('volume')),('number',w.get('issue')),('pages',w.get('pages')),('isbn',w.get('isbn'))] if v)+'\n}')
            ris.extend(['TY  - '+('BOOK' if kind=='book' else 'RPRT' if kind=='techreport' else 'CPAPER' if kind=='inproceedings' else 'JOUR'),'TI  - '+w['title'],
                *[('A2  - ' if w.get('contributors_role')=='editors' else 'AU  - ')+a for a in w['authors'].split('; ') if a],
                *(['ET  - '+str(w['edition'])] if w.get('edition') else []),'PY  - '+str(w['year'] or ''),
                'DO  - '+w['doi'],'UR  - '+w['url'],'ER  - ',''])
        (self.out/'referencias_fundamentacao.bib').write_text('\n\n'.join(bibliography))
        (self.out/'referencias_fundamentacao.ris').write_text('\n'.join(ris))
        for group in range(1,5):
            subset=[w for w in self.selected if w['topic'].startswith(str(group)+'.')]
            flatten(subset).to_csv(self.out/f'por_secao/Secao_{group}_Referencias.csv',index=False)
            lines=[f'# Fundamentação teórica da seção {group}',
               'Seleção orientada por tópico. Contagens são das bases e datas indicadas; a leitura integral pelo grupo permanece necessária.']
            for topic in [t for t in self.topics if t['id'].startswith(str(group)+'.')]:
                lines.extend(['',f'## {topic["id"]} {topic["title"]}',f'Responsável: {topic["owner"]}.'])
                for w in subset:
                    if w['topic']!=topic['id']:continue
                    lines.extend(['',f'**{w["id"]} — {w["selection_role"]}.** '+citation(w),
                      'DOI: '+(w['doi'] or 'não informado')+' · Acesso: '+(w['oa_url'] or w['url']),
                      counts(w),'Uso: '+'; '.join(w['seed_roles']) if w['seed_roles'] else 'Correspondência temática: '+w['match_reason']])
            (self.out/f'por_secao/Secao_{group}_Referencias.md').write_text('\n\n'.join(lines))
        summary={'status':'executado','purpose':self.cfg['scope'],'topics':len(self.topics),
          'normalized_records':len(self.records),'unique_works':len(self.works),'topic_assignments':len(self.links),
          'priority_assignments':len(self.selected),'unique_priority_works':len(unique),
          'sources_with_actual_records':sorted(set(r['source'] for r in self.records)),
          'source_status':self.availability.to_dict('records'),'full_text_review_completed':False,
          'ranking_scope':self.cfg['interpretation'],'generated_at':datetime.now(timezone.utc).isoformat(),
          'reference_presentation':'ABNT NBR 6023:2025; Times New Roman 12; recuo francês de 1,25 cm; catálogo alfabético e mapa dos 19 tópicos'}
        (self.out/'resumo_levantamento.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
        self.summary=summary
        write_docx(self)
        return summary

def citation(w):
    return abnt.reference_text(w)

def counts(w):
    pieces=[]
    for source in SOURCES:
        n=w.get('citations_'+source);date=w.get('citations_date_'+source)
        if n is not None:pieces.append(f'{source}: {n} citações (consulta {str(date)[:10]})')
    return '; '.join(pieces) or 'Contagem de citações não disponível; ausência não foi convertida em zero.'

def write_docx(survey):
    from word_referencias_abnt import write
    return write(survey)

def run(root,live=True):
    survey=Survey(root,live=live);survey.collect();survey.consolidate();survey.select();survey.export()
    return survey

if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser();parser.add_argument('--offline',action='store_true');args=parser.parse_args()
    result=run(Path(__file__).resolve().parent,live=not args.offline)
    print(json.dumps(result.summary,ensure_ascii=False,indent=2))
