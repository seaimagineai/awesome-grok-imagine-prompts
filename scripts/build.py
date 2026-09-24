#!/usr/bin/env python3
"""Build a task-first gallery and one workflow in fifteen languages."""
import argparse
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = ['sea-glass-bottle', 'blue-route', 'honey-loaf', 'harbor-reunion',
         'first-sip', 'salt-line', 'coastal-postcard', 'citrus-halo']
FEATURED_GROUPS = [['sea-glass-bottle', 'citrus-halo'], ['blue-route', 'coastal-postcard'],
                   ['first-sip', 'salt-line'], ['harbor-reunion'], [], [], [], ['honey-loaf'], []]
MODES = [['text','image','reference'], ['text','image','extension'], ['text','image','reference'],
         ['reference'], ['edit','extension'], ['text'], ['text'], ['text'], ['text']]
COLLECTIONS = ['01-ads-and-products', '02-cinematic-storytelling', '03-social-ugc',
               '04-characters-and-references', '05-editing-and-extension',
               '07-satisfying-materials', '08-spaces-and-transformations',
               '09-miniature-and-surreal', '10-fashion-and-performance']


def catalog():
    groups = []
    for slug in COLLECTIONS:
        text = (ROOT / 'prompts' / (slug + '.md')).read_text()
        entries = []
        for title, body in re.findall(r'^## (\d+\..+?)\n(.*?)(?=^## |\Z)', text, re.M | re.S):
            prompt = re.search(r'```text\n(.*?)\n```', body, re.S).group(1)
            anchor = re.sub(r'[^\w\-\s]', '', title.lower()).replace(' ', '-')
            entries.append((title, anchor, prompt))
        groups.append((slug, entries))
    return groups


def render_core(data, featured, product_url, guide, locale, ui):
    cases = {c['id']: c for c in data['cases'] + featured['cases']}
    source_ids = {c['id'] for c in featured['cases']}
    out = ['<a id="find-the-right-prompt"></a>', '<a id="prompt-library"></a>',
           f'## {featured["nav_title"]}', f'[{featured["browse_label"]} · 62](docs/PROMPT_INDEX.md)']
    rows = [f'| {featured["category_label"]} | {ui["scenes_label"]} | {ui["modes_label"]} | {ui["examples_label"]} |', '| --- | --- | --- | --- |']
    for n, (slug, entries) in enumerate(catalog()):
        examples = ' · '.join(f'[{cases[key]["title"]}](#case-{key})' for key in FEATURED_GROUPS[n]) or '—'
        mode_keys = list(dict.fromkeys(MODES[n] + (['image'] if FEATURED_GROUPS[n] else [])))
        modes = ' / '.join(ui['mode_names'][key] for key in mode_keys)
        count = len(entries) + len(FEATURED_GROUPS[n])
        rows.append(f'| [{ui["category_names"][n]} · {count}](docs/PROMPT_INDEX.md#{slug}) | {ui["scene_summaries"][n]} | {modes} | {examples} |')
    out.append('\n'.join(rows))
    out.append(f'[{featured["quick_links"][0]}](#featured-prompts) · [{ui["brand_label"]}](#create-with-seaimagine)')
    out += ['<a id="visual-index"></a>', '<a id="featured-prompts"></a>', f'## {featured["gallery_title"]}', featured['gallery_intro'], featured['source_note']]
    for i, ident in enumerate(ORDER, 1):
        case = cases[ident]
        out += [f'<a id="case-{ident}"></a>']
        if ident in source_ids:
            out += [f'<a id="{case["legacy_anchor"]}"></a>']
        else:
            out += [f'<a id="seaimagine-{ident}"></a>']
        out += [f'### {i}. {case["title"]}']
        if ident in ('first-sip', 'coastal-postcard'):
            out.append(f'<a href="{case["image"]}"><img src="{case["image"]}" width="480" alt="{html.escape(case["title"], quote=True)}"></a>')
        else:
            out.append(f'![{case["title"]}]({case["image"]})')
        out += [f'**{data["settings_label"]}:** {case["settings"]} · [{data["image_label"]}]({case["image"]}) · [TXT](prompts/text/{locale}/{ident}.txt)']
        if ident in source_ids:
            out.append(f'[{featured["source_label"]}](docs/ATTRIBUTION.md)')
        out.append('```text\n' + case['prompt'] + '\n```')
        out.append(f'[{featured["back_label"]}](#find-the-right-prompt)')
    out += ['<a id="seaimagine-browser-workflow"></a>', '<a id="create-with-seaimagine"></a>',
            f'## {ui["brand_title"]}', ui['brand_intro'],
            ' · '.join(f'[{label}](#case-{ident})' for label, ident in zip(ui['brand_links'], ['sea-glass-bottle','harbor-reunion','coastal-postcard'])),
            f'[![SeaImagine · Grok Imagine 1.5](assets/seaimagine-interface.jpg)]({product_url})',
            ui['brand_caption'], f'**[{ui["brand_cta"]}]({product_url})**',
            '<a id="learn-from-official-and-community-examples"></a>',
            '<a id="writing-guide"></a>']
    # Keep existing external bookmarks valid after relocating reference material.
    out.extend(f'<a id="{a}"></a>' for a in sorted(set(guide['legacy_anchors']) - {'multilingual-prompts'}))
    out += [f'## {featured["more_label"]}',
            f'[{featured["quick_links"][3]}]({guide["guide"]}) · [{featured["reference_label"]}](docs/workflows/{locale}.md) · [SeaImagine]({product_url})',
            f'[{ui["source_label"]}](docs/COMMUNITY.md) · [X / YouTube](docs/SOCIAL_INSPIRATION.md)',
            '<a id="multilingual-prompts"></a>',
            f'## {featured["counts_label"]}', data['recipe_count_note'],
            '[Flaq AI](https://github.com/flaqai/awesome-grok-imagine) · [SeaImagine]('+product_url+') · [MIT](LICENSE) · [CONTRIBUTING](CONTRIBUTING.md) · [15 languages](docs/LANGUAGES.md)']
    return '\n\n'.join(out)+'\n'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args=parser.parse_args()
    locales=json.loads((ROOT/'data/locales.json').read_text())['languages']
    guides=json.loads((ROOT/'data/guide-index.json').read_text())
    interface=json.loads((ROOT/'data/catalog-ui.json').read_text())
    nav=' · '.join(f'[{x["name"]}]({x["readme"]})' for x in locales)
    stale=[]
    def output(path, text):
        if args.check:
            if not path.exists() or path.read_text() != text: stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    index = ['# Complete prompt index', '[← Main collection](../README.md)',
             '62 distinct English prompts. Each illustrated case is listed once in its category. New original briefs are not generation-tested; [sources](SOCIAL_INSPIRATION.md).']
    en = json.loads((ROOT / 'data/homepage-locales/en-US.json').read_text())
    feat = json.loads((ROOT / 'data/featured-locales/en-US.json').read_text())
    by_id = {c['id']: c for c in en['cases'] + feat['cases']}
    labels = interface['en-US']['category_names']
    index.append(' · '.join(f'[{label}](#{slug})' for label, slug in zip(labels, COLLECTIONS)))
    for n, (slug, entries) in enumerate(catalog()):
        index += [f'<a id="{slug}"></a>', f'## {labels[n]}',
                  f'[Category prompts](../prompts/{slug}.md) · [↑ Categories](#complete-prompt-index)']
        rows = ['| Prompt / scene | Mode | Duration · ratio · resolution | Copy |', '| --- | --- | --- | --- |']
        for key in FEATURED_GROUPS[n]:
            case = by_id[key]
            rows.append(f'| [{case["title"]} · illustrated](../README.md#case-{key}) | image-to-video | {case["settings"]} | [TXT](../prompts/text/en-US/{key}.txt) |')
        body = (ROOT / 'prompts' / (slug + '.md')).read_text()
        sections = re.findall(r'^## \d+\..+?\n(.*?)(?=^## |\Z)', body, re.M | re.S)
        for (title, anchor, prompt), section in zip(entries, sections):
            mode_match = re.search(r'\*\*Mode:\*\* ([^·\n]+)', section)
            mode = mode_match.group(1).strip() if mode_match else 'reference-to-video'
            settings = re.search(r'\*\*Output:\*\* ([^\n]+)', section).group(1).strip()
            rows.append(f'| [{title}](../prompts/{slug}.md#{anchor}) | {mode} | {settings} | [TXT](../prompts/text/en-US/{slug}-{title.split(".")[0]}.txt) |')
        index.append('\n'.join(rows))
    output(ROOT / 'docs/PROMPT_INDEX.md', '\n\n'.join(index) + '\n')
    for slug, entries in catalog():
        for title, anchor, prompt in entries:
            output(ROOT / 'prompts/text/en-US' / (slug + '-' + title.split('.')[0] + '.txt'), prompt + '\n')
    for item in locales:
        data=json.loads((ROOT/'data/homepage-locales'/f'{item["locale"]}.json').read_text())
        featured=json.loads((ROOT/'data/featured-locales'/f'{item["locale"]}.json').read_text())
        for case in data['cases'] + featured['cases']:
            output(ROOT / 'prompts/text' / item['locale'] / (case['id'] + '.txt'), case['prompt'] + '\n')
        workflow = '\n\n'.join([f'# {data["workflow_title"]}', f'[← {item["name"]}](../../{item["readme"]})',
            f'[SeaImagine · Grok Imagine 1.5]({item["product_url"]})', data['workflow_intro'],
            f'![{data["workflow_title"]}](../../assets/seaimagine-interface.jpg)',
            '\n'.join(f'{i}. {step}' for i, step in enumerate(data['steps'], 1))]) + '\n'
        output(ROOT / 'docs/workflows' / (item['locale'] + '.md'), workflow)
        template=(ROOT/'templates/readmes'/item['readme']).read_text()
        rendered=template.replace('{{LANGUAGE_NAV}}',nav).replace('{{PRODUCT_URL}}',item['product_url']).replace('{{LOCALIZED_CORE}}',render_core(data,featured,item['product_url'],guides[item['locale']],item['locale'],interface[item['locale']]))
        rendered=rendered.rstrip()+'\n'
        path=ROOT/item['readme']
        if args.check:
            if not path.exists() or path.read_text()!=rendered:stale.append(item['readme'])
        else:path.write_text(rendered)
    if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
    print('15 task-first language pages '+('verified' if args.check else 'generated'))

if __name__=='__main__':main()
