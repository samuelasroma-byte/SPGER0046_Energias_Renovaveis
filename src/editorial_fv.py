"""Editorial ownership and publication paths, independent of physical modelling."""
from pathlib import Path
import json
import zipfile


def policy(root):
    path = Path(root) / 'config/distribuicao_editorial.json'
    return json.loads(path.read_text()) if path.exists() else None


def assign_figure(root, record):
    rules = policy(root)
    if rules is None:
        return record
    item = next(r for r in rules['figures'] if r['id'] == record['id'])
    record['subsections'] = [item['owner_subsection']]
    record['owner_subsection'] = item['owner_subsection']
    return record


def figure_path(root, ident, theme, fmt):
    rules = policy(root)
    if rules is None:
        return None
    item = next(r for r in rules['figures'] if r['id'] == ident)
    section = next(s for s in rules['sections'] if str(s['section']) == item['owner_subsection'][0])
    category = 'figuras/fluxogramas' if item['category'] == 'fluxogramas' else item['category']
    return Path(root) / section['directory'] / category / theme / (ident + '.' + fmt)


def assign_sections(root, sections):
    rules = policy(root)
    if rules is None:
        return sections
    result = []
    for section in sections:
        item = dict(section)
        item['figures'] = [r['id'] for r in rules['figures'] if r['owner_subsection'] == item['id']]
        result.append(item)
    return result


def zip_results(ctx):
    """Package numerical outputs and the uniquely assigned editorial assets."""
    root=Path(ctx['root'])
    target=root/'outputs/Resultados_Execucao_Projeto_FV.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as archive:
        for directory in ['outputs','secoes']:
            for path in sorted((root/directory).rglob('*')):
                if path.is_file() and path!=target:
                    archive.write(path,path.relative_to(root).as_posix())
        for relative in ['config/distribuicao_editorial.json','docs/Distribuicao_Editorial.md']:
            path=root/relative
            if path.exists():archive.write(path,relative)
    return target
