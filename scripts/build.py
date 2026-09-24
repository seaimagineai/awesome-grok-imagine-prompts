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
GOALS = ORDER[:7]
COLLECTIONS = ['01-ads-and-products', '02-cinematic-storytelling', '03-social-ugc',
               '04-characters-and-references', '05-editing-and-extension']


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


def render_core(data, featured, product_url, guide, locale):
    cases = {c['id']: c for c in data['cases'] + featured['cases']}
    source_ids = {c['id'] for c in featured['cases']}
    out = ['<a id="find-the-right-prompt"></a>', '<a id="prompt-library"></a>',
           f'## {featured["nav_title"]}',
           f'| {featured["goal_label"]} | {featured["example_label"]} |', '| --- | --- |']
    table = out[-2:]
    out = out[:-2]
    for label, ident in zip(featured['goals'], GOALS):
        links=f'[{cases[ident]["title"]}](#case-{ident})'
        if ident == 'sea-glass-bottle':
            links += f' · [{cases["citrus-halo"]["title"]}](#case-citrus-halo)'
        table.append(f'| {label} | {links} |')
    out.append('\n'.join(table))
    out.append(' · '.join([f'[{featured["quick_links"][0]}](#featured-prompts)',
        f'[{featured["quick_links"][2]}](#learn-from-official-and-community-examples)',
        f'[{featured["reference_label"]}](#writing-guide)']))
    out += ['<a id="visual-index"></a>', f'### {featured["preview_title"]}', featured['gallery_intro'], featured['source_note']]
    preview = ['| | |', '| --- | --- |']
    for a, b in zip(ORDER[::2], ORDER[1::2]):
        cells = []
        for ident in (a, b):
            c = cases[ident]
            cells.append(f'<a href="#case-{ident}"><img src="{c["image"]}" height="180" alt="{html.escape(c["title"], quote=True)}"></a><br>[{ORDER.index(ident)+1}. {c["title"]}](#case-{ident})<br>{c["settings"]}')
        preview.append('| ' + ' | '.join(cells) + ' |')
    out.append('\n'.join(preview))
    out.append(f'**{featured["browse_label"]} · 30**')
    rows = [f'| {featured["category_label"]} | {featured["browse_cases_label"]} |', '| --- | --- |']
    for label, (slug, entries) in zip(featured['collections'], catalog()):
        links = ' · '.join(f'[{title}](prompts/{slug}.md#{anchor})' for title, anchor, _ in entries)
        rows.append(f'| [{label} · {len(entries)}](prompts/{slug}.md) | {links} |')
    out.append('\n'.join(rows))
    out += ['<a id="featured-prompts"></a>', f'## {featured["gallery_title"]}']
    for i, ident in enumerate(ORDER, 1):
        case = cases[ident]
        out += [f'<a id="case-{ident}"></a>']
        if ident in source_ids:
            out += [f'<a id="{case["legacy_anchor"]}"></a>']
        else:
            out += [f'<a id="seaimagine-{ident}"></a>']
        out += [f'### {i}. {case["title"]}']
        out += [f'**{data["settings_label"]}:** {case["settings"]} · [{data["image_label"]}]({case["image"]}) · [TXT](prompts/text/{locale}/{ident}.txt)']
        if ident in source_ids:
            out.append(f'[{featured["source_label"]}](docs/ATTRIBUTION.md)')
        out.append('```text\n' + case['prompt'] + '\n```')
        out.append(f'[{featured["back_label"]}](#find-the-right-prompt) · [{featured["preview_title"]}](#visual-index)')
    out += ['<a id="learn-from-official-and-community-examples"></a>',
            f'## {data["community_title"]}', data['community_intro']]
    thumbs = {0:'https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg',
              2:'https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg'}
    for i,item in enumerate(data['community_items']):
        out.append(f'### [{item["title"]}]({item["url"]})')
        if i in thumbs:
            out.append(f'[![{item["title"]}]({thumbs[i]})]({item["url"]})')
        out.append(item['text'])
    out += ['<details>\n<summary>'+html.escape(featured['community_details'])+'</summary>\n\n'+data['viewing_note']+'\n\n</details>',
            f'[{data["source_details_label"]}](docs/COMMUNITY.md)',
            '<a id="writing-guide"></a>']
    # Keep existing external bookmarks valid after relocating reference material.
    out.extend(f'<a id="{a}"></a>' for a in sorted(set(guide['legacy_anchors']) - {'multilingual-prompts'}))
    out += [f'## {featured["more_label"]}',
            f'[{featured["quick_links"][3]}]({guide["guide"]}) · [{featured["reference_label"]}](docs/workflows/{locale}.md) · [SeaImagine]({product_url})',
            '<a id="seaimagine-browser-workflow"></a>', '<a id="create-with-seaimagine"></a>',
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
    nav=' · '.join(f'[{x["name"]}]({x["readme"]})' for x in locales)
    stale=[]
    def output(path, text):
        if args.check:
            if not path.exists() or path.read_text() != text: stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
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
        rendered=template.replace('{{LANGUAGE_NAV}}',nav).replace('{{PRODUCT_URL}}',item['product_url']).replace('{{LOCALIZED_CORE}}',render_core(data,featured,item['product_url'],guides[item['locale']],item['locale']))
        rendered=rendered.rstrip()+'\n'
        path=ROOT/item['readme']
        if args.check:
            if not path.exists() or path.read_text()!=rendered:stale.append(item['readme'])
        else:path.write_text(rendered)
    if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
    print('15 task-first language pages '+('verified' if args.check else 'generated'))

if __name__=='__main__':main()
