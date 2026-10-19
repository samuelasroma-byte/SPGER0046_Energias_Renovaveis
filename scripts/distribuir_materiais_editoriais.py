"""Publish one editorial owner per figure, CSV, logical table and frame.

Only paths, catalogues and navigation are changed. The original numerical
CSVs, graphic bytes and consolidated source documents are preserved.
"""
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit
import csv
import hashlib
import json
import os
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / 'config/distribuicao_editorial.json'


def write_csv(path, rows, fields=None):
    with path.open('w', encoding='utf-8-sig', newline='') as handle:
        writer = csv.DictWriter(handle, fields or list(rows[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)


def link(page, target, label):
    return '[' + label + '](' + Path(os.path.relpath(ROOT / target, page.parent)).as_posix() + ')'


def main():
    policy = json.loads(POLICY.read_text())
    sections = {str(s['section']): s for s in policy['sections']}
    owners = {f['id']: f for f in policy['figures']}
    inventory_path = ROOT / 'docs/auditoria/Inventario_Figuras.json'
    figures = json.loads(inventory_path.read_text())
    moves = {}
    for figure in figures:
        item = owners[figure['id']]
        owner = item['owner_subsection']
        folder = sections[owner[0]]['directory']
        category = 'figuras/fluxogramas' if figure['category'] == 'fluxogramas' else figure['category']
        for variant, old in figure['files'].items():
            theme, fmt = variant.split('_')
            new = f"{folder}/{category}/{theme}/{figure['id']}.{fmt}"
            if old != new:
                assert (ROOT / old).is_file() and not (ROOT / new).exists(), (old, new)
                (ROOT / new).parent.mkdir(parents=True, exist_ok=True)
                shutil.move(ROOT / old, ROOT / new)
                moves[old] = new
            figure['files'][variant] = new
        figure['subsections'] = owner
        figure['owner_subsection'] = owner
        figure['owner_section'] = int(owner[0])
    inventory_path.write_text(json.dumps(figures, ensure_ascii=False, indent=2) + '\n')
    figures_by_id = {f['id']: f for f in figures}

    # Keep the active provenance inventories accurate after byte-preserving moves.
    p = ROOT / 'docs/auditoria/Proveniencia_Arquivos_Integrados.json'
    records = json.loads(p.read_text())
    for row in records:
        row['caminho_github'] = moves.get(row['caminho_github'], row['caminho_github'])
    p.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    write_csv(p.with_suffix('.csv'), records)
    p = ROOT / 'docs/auditoria/Inventario_Drive_Completo.csv'
    rows = list(csv.DictReader(p.open(encoding='utf-8-sig')))
    for row in rows:
        row['caminho_github'] = moves.get(row['caminho_github'], row['caminho_github'])
    write_csv(p, rows)
    p = ROOT / 'docs/auditoria/Inventario_Figuras.csv'
    rows = list(csv.DictReader(p.open(encoding='utf-8-sig')))
    for row in rows:
        owner = owners[row['id']]['owner_subsection']
        for key, value in list(row.items()):
            for old, new in moves.items():
                value = value.replace(old, new)
            row[key] = owner if key in ['subsections', 'subsecoes'] else value
    write_csv(p, rows)
    write_csv(ROOT / 'docs/auditoria/Distribuicao_Tabelas.csv', [
        {'arquivo': r['path'], 'subsecoes': r['owner_subsection'],
         'criterio': 'uma única subseção responsável; dados e valores preservados'}
        for r in policy['csv_tables']])

    # Update links outside the historical source snapshots before rewriting indices.
    for page in ROOT.rglob('*.md'):
        if '.git' in page.parts or 'originais' in page.parts:
            continue
        text = page.read_text()
        def remap(match):
            target = match[1]
            if urlsplit(target).scheme or target.startswith('#'):
                return match[0]
            resolved = (page.parent / target.split('#', 1)[0]).resolve()
            try:
                relative = resolved.relative_to(ROOT).as_posix()
            except ValueError:
                return match[0]
            if relative not in moves:
                return match[0]
            return '](' + Path(os.path.relpath(ROOT / moves[relative], page.parent)).as_posix() + ')'
        updated = re.sub(r'\]\(([^\n]*?)\)', remap, text)
        if updated != text:
            page.write_text(updated)

    def figure_table(page, selected):
        if not selected:
            return 'Não há ilustração atribuída a este conjunto.\n'
        text = '| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |\n| --- | --- | --- | --- |\n'
        for f in selected:
            text += '| ' + f['id'] + ' — ' + f['title'] + ' | ' + f['owner_subsection'] + ' | '
            text += ' / '.join(link(page, f['files'][theme+'_png'], theme.capitalize()) for theme in ['claro','escuro']) + ' | '
            text += ' / '.join(link(page, f['files'][theme+'_pdf'], theme.capitalize()) for theme in ['claro','escuro']) + ' |\n'
        return text

    def csv_table(page, selected):
        if not selected:
            return 'Não há CSV de tabela atribuído a esta subseção.\n'
        text = '| Dados e tabelas em CSV | Inserir em |\n| --- | --- |\n'
        for item in selected:
            text += '| ' + link(page, item['path'], item['id']) + ' | ' + item['owner_subsection'] + ' |\n'
        return text

    def logical_table(page, selected, word_path):
        if not selected:
            return 'Não há tabela ou quadro Word atribuído a esta subseção.\n'
        text = '| ID | Tabela ou quadro | Inserir em |\n| --- | --- | --- |\n'
        for item in selected:
            text += f"| {item['id']} | {item['title']} | {item['owner_subsection']} |\n"
        return text + '\n' + link(page, word_path, 'Baixar o Word com os materiais tabulares desta seção') + '.\n'

    rule = ('Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. '
            'Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.\n')
    words = policy['word_tables'] + policy['frames']
    for number, section in sections.items():
        folder = ROOT / section['directory']
        own_figs = [f for f in figures if str(f['owner_section']) == number]
        own_csv = [r for r in policy['csv_tables'] if r['owner_subsection'][0] == number]
        own_words = [r for r in words if r['owner_subsection'][0] == number]
        word_path = section['directory'] + f'/tabelas/docx/Materiais_Tabulares_Secao_{int(number):02d}.docx'
        page = folder / 'README.md'
        text = re.split(r'## (?:Ilustrações pertinentes|Materiais exclusivos desta seção)', page.read_text(), maxsplit=1)[0]
        text += '## Materiais exclusivos desta seção\n\n' + rule + '\n' + figure_table(page, own_figs)
        text += '\n' + link(page, section['directory']+'/tabelas/README.md', 'Tabelas e séries da seção')
        text += ' · ' + link(page, section['directory']+'/quadros/README.md', 'Quadros da seção')
        text += ' · ' + link(page, word_path, 'Word exclusivo desta seção') + '\n\n'
        text += link(page, 'docs/Distribuicao_Editorial.md', 'Mapa geral e regra de inserção única') + '\n'
        if (folder/'equacoes/README.md').exists():
            text += '\n## Equações da seção\n\n[Ler as equações em PDF ou abrir o Word editável](equacoes/README.md).\n'
        page.write_text(text)

        for category in ['figuras', 'graficos']:
            page = folder / category / 'README.md'
            selected = [f for f in own_figs if f['category'] == category or category == 'figuras' and f['category'] == 'fluxogramas']
            page.write_text(f'# {category.capitalize()} da seção {number}\n\n' + rule + '\n' + figure_table(page, selected)
                            + '\n' + link(page, 'docs/Distribuicao_Editorial.md', 'Mapa de inserção única') + '\n')
        page = folder / 'tabelas/README.md'
        selected = [r for r in policy['word_tables'] if r['owner_subsection'][0] == number]
        page.write_text(f'# Tabelas da seção {number}\n\n' + rule + '\n' + logical_table(page, selected, word_path)
                        + '\n## Arquivos numéricos desta seção\n\n' + csv_table(page, own_csv)
                        + '\nOs CSVs conservam os caminhos usados no cálculo; cada arquivo tem uma única seção responsável para a redação.\n')
        page = folder / 'quadros/README.md'
        selected = [r for r in policy['frames'] if r['owner_subsection'][0] == number]
        page.write_text(f'# Quadros da seção {number}\n\n' + rule + '\n' + logical_table(page, selected, word_path))

        page = folder / 'documentos/README.md'
        page.write_text(f'# Documentos para a seção {number}\n\n'
                        + link(page, word_path, 'Materiais tabulares exclusivos desta seção') + '\n\n'
                        + '## Documentos comuns de orientação\n\nEstes documentos apoiam a leitura dos dados e a organização da equipe. A seleção de ilustrações e tabelas para inserir está exclusivamente nos índices da seção.\n\n'
                        + '\n'.join('- ' + link(page, target, title) for title,target in [
                            ('Guia técnico resumido', 'docs/metodos/Guia_Tecnico_Resumido_PVDAQ_2107.docx'),
                            ('Dossiê técnico dos dados e equipamentos', 'docs/metodos/Dossie_Tecnico_por_Secao.docx'),
                            ('Proposta oficial do capítulo', 'docs/planejamento/Proposta_do_Capitulo_Recurso_Solar_FV.docx'),
                            ('Referências por subseção', 'bibliografia/principal/README.md')]) + '\n')

        equation_word=folder/f'equacoes/Quadro_Equacoes_Secao_{int(number):02d}.docx'
        if equation_word.exists():
            page.write_text(page.read_text()+'\n[Quadro de equações exclusivo desta seção em PDF e Word](../equacoes/README.md).\n')

        for page in folder.glob('subsecoes/*/README.md'):
            subsection = page.parent.name.replace('_','.')
            text = page.read_text()
            start = re.search(r'## (?:Figuras, gráficos e fluxograma|Ilustrações de inserção exclusiva)', text).start()
            end = text.index('## Documentos, dados e execução')
            selected = [f for f in own_figs if f['owner_subsection'] == subsection]
            new = '## Ilustrações de inserção exclusiva\n\n' + rule + '\n' + figure_table(page, selected)
            for f in selected:
                new += '\n**' + f['id'] + ':** ' + f['caption'] + ' Fonte: ' + f['source'] + ' Métodos: ' + f['refs'] + '.\n'
            new += '\n## Tabelas e quadros de inserção exclusiva\n\n'
            new += logical_table(page, [r for r in own_words if r['owner_subsection']==subsection], word_path)
            new += '\n' + csv_table(page, [r for r in own_csv if r['owner_subsection']==subsection]) + '\n'
            text = text[:start] + new + text[end:]
            text = re.sub(r' · \[Word completo dos gráficos\]\([^)]*\)', '', text)
            page.write_text(text)

    # The active chapter matrices and the notebook builder use exactly the same owners.
    p = ROOT / 'docs/secoes_capitulo.json'
    rows = json.loads(p.read_text())
    for row in rows:
        row['figures'] = [f['id'] for f in policy['figures'] if f['owner_subsection'] == row['id']]
    p.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    p = ROOT / 'docs/Matriz_19_Subsecoes.md'
    text = p.read_text()
    for row in rows:
        pattern = r'(## '+re.escape(row['id'])+r' [\s\S]*?)(?=\n## |\Z)'
        match = re.search(pattern, text)
        if match:
            block = re.sub(r'\*\*Figuras[^\n]*', '**Figuras de inserção exclusiva:** ' + ', '.join(row['figures']) + '.', match[1])
            text = text[:match.start()] + block + text[match.end():]
    p.write_text(text)
    p = ROOT / 'figuras/README.md'
    text = '# Catálogo de ilustrações com inserção única\n\n' + rule + '\n'
    for number, section in sections.items():
        text += '## Seção ' + number + '\n\n' + figure_table(p, [f for f in figures if str(f['owner_section'])==number]) + '\n'
    text += '## Legendas e fontes\n\n'
    for f in figures:
        text += '### ' + f['id'] + '\n\n**Inserir em ' + f['owner_subsection'] + '.** ' + f['caption'] + '\n\nFonte: '+f['source']+' Métodos: '+f['refs']+'.\n\n'
    p.write_text(text.rstrip()+'\n')
    (ROOT/'docs/Catalogo_Figuras.md').write_text('# Catálogo editorial das figuras\n\n[Ilustrações com uma única subseção de inserção](../figuras/README.md).\n\n[Mapa de responsabilidade e justificativas](Distribuicao_Editorial.md).\n')
    write_csv(ROOT/'docs/Catalogo_Figuras.csv', [{k:v for k,v in f.items() if k not in ['files','resolution']} for f in figures])
    p = ROOT/'outputs/tabelas/README.md'
    p.write_text('# Catálogo de tabelas com inserção única\n\n' + rule + '\n' + csv_table(p, policy['csv_tables'])
                 + '\n## Documentos por seção\n\n' + '\n'.join('- '+link(p, s['directory']+f"/tabelas/docx/Materiais_Tabulares_Secao_{s['section']:02d}.docx", 'Word da seção '+str(s['section'])) for s in policy['sections'])
                 + '\n\nA coleção consolidada reúne as tabelas do projeto. Os documentos por seção identificam os itens usados na redação. A Tabela 16 possui quatro blocos de continuação e conta como uma única tabela.\n')
    p = ROOT/'docs/Distribuicao_Editorial.md'
    text = '# Distribuição editorial sem repetição\n\n' + rule
    text += '\nUsar os IDs estáveis na redação, por exemplo «Figura G04» ou «Tabela T10». A numeração sequencial final será aplicada na consolidação do capítulo. Um mesmo CSV pode alimentar cálculos diversos, mas sua inclusão editorial pertence apenas à subseção indicada.\n\n'
    for number, section in sections.items():
        text += '## Seção ' + number + ' ' + section['title'] + '\n\n**Responsáveis:** ' + section['responsible'] + '.\n\n'
        text += '| Material | Inserir em | Motivo |\n| --- | --- | --- |\n'
        for item in policy['figures']:
            if item['owner_subsection'][0] == number:
                text += '| '+item['id']+' — '+item['title']+' | '+item['owner_subsection']+' | '+item['reason']+' |\n'
        text += '\n| Tabela ou quadro | Inserir em |\n| --- | --- |\n'
        for item in words:
            if item['owner_subsection'][0] == number:
                text += '| '+item['id']+' — '+item['title']+' | '+item['owner_subsection']+' |\n'
        text += '\n' + link(p, section['directory']+'/README.md', 'Abrir apenas os materiais desta seção') + '\n\n'
    text += '## Fontes e preservação\n\nA atribuição segue a proposta oficial de quatro seções e 19 subseções, as células do notebook e a natureza de cada resultado. Há 30 ilustrações em 120 arquivos PNG/PDF e 24 CSVs de resultados tabulares. Há 16 tabelas lógicas no Word original, distribuídas em 19 blocos porque a T16 continua em quatro partes, e seis quadros. Os documentos por seção preservam as tabelas editáveis e identificam seu único local de inserção.\n\n'
    text += 'Os índices e os documentos por seção seguem a distribuição definida em [distribuicao_editorial.json](../config/distribuicao_editorial.json).\n'
    p.write_text(text)
    print(json.dumps({'figures':len(figures),'CSV_files':len(policy['csv_tables']),
                      'logical_Word_tables':len(policy['word_tables']),'frames':len(policy['frames']),
                      'graphic_files_moved':len(moves)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
