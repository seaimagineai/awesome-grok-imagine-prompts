#!/usr/bin/env python3
"""Render language navigation from the website locale manifest. No dependencies."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    locales = json.loads((ROOT / 'data/locales.json').read_text())['languages']
    nav = ' · '.join(f'[{x["name"]}]({x["readme"]})' for x in locales)
    stale = []
    for item in locales:
        name = item['readme']
        template = (ROOT / 'templates/readmes' / name).read_text()
        rendered = template.replace('{{LANGUAGE_NAV}}', nav).replace('{{PRODUCT_URL}}', item['product_url'])
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != rendered:
                stale.append(name)
        else:
            path.write_text(rendered)
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print('15 language pages ' + ('verified' if args.check else 'generated'))

if __name__ == '__main__':
    main()
