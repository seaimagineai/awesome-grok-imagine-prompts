#!/usr/bin/env python3
"""Build a task-first gallery and one workflow in fifteen languages."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ORDER = ['sea-glass-bottle', 'blue-route', 'honey-loaf', 'harbor-reunion',
         'first-sip', 'salt-line', 'coastal-postcard', 'citrus-halo']
GOALS = ORDER[:7]
COLLECTIONS = ['01-ads-and-products', '02-cinematic-storytelling', '03-social-ugc',
               '04-characters-and-references', '05-editing-and-extension']


def render_core(data, featured, product_url, guide):
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
    out.append(f'**{featured["browse_label"]}:** ' + ' · '.join(
        f'[{label}](prompts/{slug}.md)' for label, slug in zip(featured['collections'], COLLECTIONS)))
    out.append(' · '.join(f'[{label}](#{anchor})' for label, anchor in zip(
        featured['quick_links'], ['featured-prompts', 'seaimagine-browser-workflow',
        'learn-from-official-and-community-examples', 'writing-guide'])))
    out += ['<a id="featured-prompts"></a>', f'## {featured["gallery_title"]}',
            featured['gallery_intro'], featured['source_note']]
    for i, ident in enumerate(ORDER, 1):
        case = cases[ident]
        out += [f'<a id="case-{ident}"></a>']
        if ident in source_ids:
            out += [f'<a id="{case["legacy_anchor"]}"></a>']
        else:
            out += [f'<a id="seaimagine-{ident}"></a>']
        out += [f'### {i}. {case["title"]}']
        if ident in ('coastal-postcard', 'first-sip'):
            out.append(f'<a href="{case["image"]}"><img src="{case["image"]}" width="420" alt="{html.escape(case["title"], quote=True)}"></a>')
        else:
            out.append(f'![{case["title"]}]({case["image"]})')
        out += [f'[{data["image_label"]}]({case["image"]})',
                f'**{data["settings_label"]}:** {case["settings"]}']
        if ident in source_ids:
            out.append(f'[{featured["source_label"]}](docs/ATTRIBUTION.md) · [{featured["quick_links"][1]}](#seaimagine-browser-workflow)')
        out.append('```text\n' + case['prompt'] + '\n```')
        if 'review' in case:
            out.append(f'**{data["review_label"]}:** {case["review"]}')
    out += ['<a id="seaimagine-browser-workflow"></a>', '<a id="create-with-seaimagine"></a>',
            f'## {data["workflow_title"]}', f'[SeaImagine · Grok Imagine 1.5]({product_url})',
            data['workflow_intro'], f'![{data["workflow_title"]}](assets/seaimagine-interface.jpg)',
            '\n'.join(f'{i}. {s}' for i,s in enumerate(data['steps'],1))]
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
            f'[{featured["quick_links"][3]}]({guide["guide"]})',
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
    for item in locales:
        data=json.loads((ROOT/'data/homepage-locales'/f'{item["locale"]}.json').read_text())
        featured=json.loads((ROOT/'data/featured-locales'/f'{item["locale"]}.json').read_text())
        template=(ROOT/'templates/readmes'/item['readme']).read_text()
        rendered=template.replace('{{LANGUAGE_NAV}}',nav).replace('{{PRODUCT_URL}}',item['product_url']).replace('{{LOCALIZED_CORE}}',render_core(data,featured,item['product_url'],guides[item['locale']]))
        rendered=rendered.rstrip()+'\n'
        path=ROOT/item['readme']
        if args.check:
            if not path.exists() or path.read_text()!=rendered:stale.append(item['readme'])
        else:path.write_text(rendered)
    if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
    print('15 task-first language pages '+('verified' if args.check else 'generated'))

if __name__=='__main__':main()
