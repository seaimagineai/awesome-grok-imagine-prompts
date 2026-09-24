#!/usr/bin/env python3
"""Build fifteen reader-facing homepages from localized editorial data."""
import argparse
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render_core(data, product_url):
    out = [f'## {data["section_title"]}', data['intro'], data['recipe_count_note']]
    out.append(' · '.join(f'[{x["title"]}](#seaimagine-{x["id"]})' for x in data['cases']))
    for i, case in enumerate(data['cases'], 1):
        out += [f'<a id="seaimagine-{case["id"]}"></a>', f'### {i}. {case["title"]}']
        if case['id'] == 'coastal-postcard':
            out.append(f'<a href="{case["image"]}"><img src="{case["image"]}" width="420" alt="{html.escape(case["title"], quote=True)}"></a>')
        else:
            out.append(f'![{case["title"]}]({case["image"]})')
        out += [f'[{data["image_label"]}]({case["image"]})', f'**{data["settings_label"]}:** {case["settings"]}', '```text\n'+case['prompt']+'\n```', f'**{data["review_label"]}:** {case["review"]}']
    out += ['<a id="seaimagine-browser-workflow"></a>', f'## {data["workflow_title"]}', f'[SeaImagine · Grok Imagine 1.5]({product_url})', data['workflow_intro'], f'![{data["workflow_title"]}](assets/seaimagine-interface.jpg)']
    out.append('\n'.join(f'{i}. {step}' for i, step in enumerate(data['steps'],1)))
    out += ['<a id="learn-from-official-and-community-examples"></a>',f'## {data["community_title"]}', data['community_intro'], data['viewing_note']]
    thumbs = {0:'https://pbs.twimg.com/amplify_video_thumb/2062223812490358785/img/jq60CyfHvCahTVW9.jpg',2:'https://pbs.twimg.com/amplify_video_thumb/2061361400409452544/img/iMwjLXsXiNr1YSXn.jpg'}
    for i,item in enumerate(data['community_items']):
        out += [f'### [{item["title"]}]({item["url"]})']
        if i in thumbs:
            out += [f'[![{item["title"]}]({thumbs[i]} )]({item["url"]})'.replace(' )',')')]
        out += [item['text']]
    out += [f'[{data["source_details_label"]}](docs/COMMUNITY.md)',f'## {data["archive_label"]}', data['archive_note']]
    return '\n\n'.join(out)+'\n'


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args=parser.parse_args()
    locales=json.loads((ROOT/'data/locales.json').read_text())['languages']
    nav=' · '.join(f'[{x["name"]}]({x["readme"]})' for x in locales)
    stale=[]
    for item in locales:
        data=json.loads((ROOT/'data/homepage-locales'/f'{item["locale"]}.json').read_text())
        template=(ROOT/'templates/readmes'/item['readme']).read_text()
        rendered=template.replace('{{LANGUAGE_NAV}}',nav).replace('{{PRODUCT_URL}}',item['product_url']).replace('{{LOCALIZED_CORE}}',render_core(data,item['product_url']))
        path=ROOT/item['readme']
        if args.check:
            if not path.exists() or path.read_text()!=rendered:stale.append(item['readme'])
        else:path.write_text(rendered)
    if stale:raise SystemExit('Stale generated files: '+', '.join(stale))
    print('15 language pages '+('verified' if args.check else 'generated'))

if __name__=='__main__':main()
