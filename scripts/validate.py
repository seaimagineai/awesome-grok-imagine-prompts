#!/usr/bin/env python3
"""Check local navigation, language coverage, provenance and recipe counts."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
errors = []

def require(ok, message):
    if not ok:
        errors.append(message)

def anchors(text):
    result = set(re.findall(r'<a\s+(?:id|name)="([^"]+)"', text))
    counts = {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\-\s]', '', title.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug if n == 0 else f'{slug}-{n}')
    return result

locales = json.loads((ROOT / 'data/locales.json').read_text())['languages']
require(len(locales) == 15, 'Expected 15 website languages')
require(len({x['locale'] for x in locales}) == 15, 'Duplicate locale')
for item in locales:
    text = (ROOT / item['readme']).read_text()
    require('```text\n' in text, item['readme'] + ': no complete prompt')
    require(item['product_url'] in text, item['readme'] + ': missing localized product URL')
    require('flaqai/awesome-grok-imagine' in text, item['readme'] + ': missing upstream attribution')
    require(all(f']({x["readme"]})' in text for x in locales), item['readme'] + ': incomplete language navigation')

for path in ROOT.rglob('*.md'):
    if '.git' in path.parts or 'templates' in path.parts:
        continue
    text = path.read_text()
    require(text.count('```') % 2 == 0, f'{path.name}: unbalanced code fences')
    require('docs/FLAQ_AI.md' not in text and 'https://flaq.ai/' not in text, f'{path.name}: stale provider route')
    require('/Users/' not in text, f'{path.name}: private local path')
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text):
        if re.match(r'^[a-zA-Z][\w+.-]*:', target):
            continue
        target = unquote(target)
        name, _, anchor = target.partition('#')
        dest = (path.parent / name).resolve() if name else path
        require(dest.exists(), f'{path.relative_to(ROOT)}: missing {target}')
        if anchor and dest.exists() and dest.suffix == '.md':
            require(anchor in anchors(dest.read_text()), f'{path.relative_to(ROOT)}: missing anchor {target}')

readme = (ROOT / 'README.md').read_text()
featured = readme.split('## Featured prompts')[1].split('\n## ')[0]
require(len(re.findall(r'```text\n', featured)) == 5, 'Expected five full featured prompts')
require(len(re.findall(r'!\[', featured)) == 5, 'Expected five featured images')
require(sum(len(re.findall(r'^## \d+\.', p.read_text(), re.M)) for p in (ROOT / 'prompts').glob('0[1-5]-*.md')) == 30, 'Expected 30 inherited category recipes')
require(len(re.findall(r'^## \d+\.', (ROOT / 'prompts/06-community-exercises.md').read_text(), re.M)) == 3, 'Expected three new exercises')
require('Copyright (c) 2026 Flaq AI' in (ROOT / 'LICENSE').read_text(), 'Missing upstream copyright')
for asset in json.loads((ROOT / 'data/assets.json').read_text()):
    p = ROOT / asset['file']
    require(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == asset['sha256'], 'Changed or missing asset: ' + asset['file'])
subprocess.run([sys.executable, str(ROOT / 'scripts/build.py'), '--check'], check=True)
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: links, anchors, 15 locales, 38 English recipes, provenance and assets')
