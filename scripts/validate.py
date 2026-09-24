#!/usr/bin/env python3
"""Check localized content, local navigation, provenance and generated pages."""
import hashlib
import json
import re
import subprocess
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []


def require(ok, message):
    if not ok:
        errors.append(message)


def anchors(text):
    result = set(re.findall(r'<[^>]+\b(?:id|name)=[\"\']([^\"\']+)[\"\']', text))
    counts = {}
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        slug = re.sub(r'[^\w\-\s]', '', title.lower()).replace(' ', '-')
        n = counts.get(slug, 0)
        counts[slug] = n + 1
        result.add(slug if n == 0 else f'{slug}-{n}')
    return result


class HTMLTargets(HTMLParser):
    """Collect links and images that Markdown link matching cannot see."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.targets = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if key in ('href', 'src') and value:
                self.targets.append(value)
            if tag == 'img' and key == 'src' and value:
                self.images.append(value)


def check_target(path, target):
    parts = urlsplit(target)
    if parts.scheme or parts.netloc:
        return
    name, anchor = unquote(parts.path), unquote(parts.fragment)
    dest = (path.parent / name).resolve() if name else path
    require(dest.exists(), f'{path.relative_to(ROOT)}: missing {target}')
    if anchor and dest.exists() and dest.suffix == '.md':
        require(anchor in anchors(dest.read_text()), f'{path.relative_to(ROOT)}: missing anchor {target}')


def same_schema(value, master, location):
    """Require all master fields and nonempty strings, including nested lists."""
    if type(value) is not type(master):
        require(False, f'{location}: incorrect JSON type')
        return False
    valid = True
    if isinstance(master, dict):
        require(value.keys() == master.keys(), f'{location}: incorrect JSON fields')
        valid = value.keys() == master.keys()
        for key in value.keys() & master.keys():
            valid = same_schema(value[key], master[key], f'{location}.{key}') and valid
    elif isinstance(master, list):
        require(len(value) == len(master), f'{location}: incorrect item count')
        valid = len(value) == len(master)
        for i, (child, expected) in enumerate(zip(value, master)):
            valid = same_schema(child, expected, f'{location}[{i}]') and valid
    elif isinstance(master, str):
        require(bool(value.strip()), f'{location}: empty text')
        valid = bool(value.strip())
    return valid


locales = json.loads((ROOT / 'data/locales.json').read_text())['languages']
require(len(locales) == 15, 'Expected 15 website languages')
require(len({x['locale'] for x in locales}) == 15, 'Duplicate locale')
locale_dir = ROOT / 'data/homepage-locales'
require({p.stem for p in locale_dir.glob('*.json')} == {x['locale'] for x in locales}, 'Homepage JSON languages differ from website manifest')
master = json.loads((locale_dir / 'en-US.json').read_text())
fixed_cases = [
    ('harbor-reunion', 'assets/seaimagine-harbor-reunion.webp', '10s · 16:9 · 720p'),
    ('coastal-postcard', 'assets/seaimagine-coastal-postcard.webp', '5s · 9:16 · 720p'),
    ('sea-glass-bottle', 'assets/seaimagine-sea-glass-bottle.webp', '5s · 16:9 · 720p'),
]
fixed_urls = [
    'https://x.com/grok/status/2062225080843747351',
    'https://x.com/JSFILMZ0412/status/2062480692835938771',
    'https://x.com/genel_ai/status/2061382998873034825',
    'https://x.com/JSFILMZ0412/status/2061117682515050669',
]
require(len(master['cases']) == 3 and len(master['steps']) == 5 and len(master['community_items']) == 4, 'English master must contain 3 cases, 5 steps and 4 community explanations')
for item in locales:
    label = item['readme']
    text = (ROOT / label).read_text()
    require('```text\n' in text, label + ': no complete prompt')
    require(item['product_url'] in text, label + ': missing localized product URL')
    require('flaqai/awesome-grok-imagine' in text, label + ': missing upstream attribution')
    require(all(f']({x["readme"]})' in text for x in locales), label + ': incomplete language navigation')
    data_path = locale_dir / f'{item["locale"]}.json'
    if not data_path.exists():
        require(False, f'Missing locale JSON: {data_path.name}')
        continue
    data = json.loads(data_path.read_text())
    if not same_schema(data, master, data_path.name):
        continue
    html_targets = HTMLTargets()
    html_targets.feed(text)
    images = set(re.findall(r'!\[[^\]]*\]\(([^\s)]+)', text)) | set(html_targets.images)
    for case, fixed in zip(data['cases'], fixed_cases):
        require(tuple(case[k] for k in ('id', 'image', 'settings')) == fixed, f'{data_path.name}: changed case identifiers, image or settings: {fixed[0]}')
        require(len(case['prompt']) <= 2000, f'{data_path.name}: prompt exceeds 2,000 characters: {fixed[0]}')
        require(f'```text\n{case["prompt"]}\n```' in text, f'{label}: missing complete prompt: {fixed[0]}')
        require(case['image'] in images, f'{label}: missing displayed starting image: {fixed[0]}')
        require((ROOT / 'prompts/text' / item['locale'] / (case['id'] + '.txt')).read_text().rstrip('\n') == case['prompt'], f'{label}: TXT differs from prompt')
    workflow = (ROOT / 'docs/workflows' / (item['locale'] + '.md')).read_text()
    require('../../assets/seaimagine-interface.jpg' in workflow, f'{label}: missing reference screenshot')
    for i, step in enumerate(data['steps'], 1):
        require(f'{i}. {step}' in workflow, f'{label}: missing browser step {i}')
    for community, expected in zip(data['community_items'], fixed_urls):
        require(community['url'] == expected, f'{data_path.name}: changed community source URL')
        require(community['text'] in text and expected in text, f'{label}: missing community explanation or source: {expected}')

for path in ROOT.rglob('*.md'):
    if '.git' in path.parts or 'templates' in path.parts:
        continue
    text = path.read_text()
    require(text.count('```') % 2 == 0, f'{path.name}: unbalanced code fences')
    require('docs/FLAQ_AI.md' not in text and 'https://flaq.ai/' not in text, f'{path.name}: stale provider route')
    require('/Users/' not in text, f'{path.name}: private local path')
    for target in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text):
        check_target(path, target)
    html_targets = HTMLTargets()
    html_targets.feed(text)
    for target in html_targets.targets:
        check_target(path, target)

readme = (ROOT / 'README.md').read_text()
featured_master = json.loads((ROOT / 'data/featured-locales/en-US.json').read_text())
provenance = json.loads((ROOT / 'data/source-featured-provenance.json').read_text())
for case, record in zip(featured_master['cases'], provenance['cases']):
    require(case['id'] == record['id'] and case['image'] == record['image'], 'Source case/image pairing changed')
    require(hashlib.sha256(case['prompt'].encode()).hexdigest() == record['prompt_sha256'], 'Source prompt changed: ' + case['id'])
for item in locales:
    label = item['readme']
    text = (ROOT / label).read_text()
    path = ROOT / 'data/featured-locales' / (item['locale'] + '.json')
    require(path.exists(), 'Missing featured translation: ' + item['locale'])
    if not path.exists():
        continue
    data = json.loads(path.read_text())
    same_schema(data, featured_master, path.name)
    for case, source in zip(data['cases'], featured_master['cases']):
        require(all(case[k] == source[k] for k in ('id', 'image', 'settings', 'legacy_anchor')), 'Changed source metadata: ' + item['locale'] + ':' + source['id'])
        require(case['prompt'] in text and case['image'] in text, label + ': missing full localized source case')
        require(len(case['prompt']) <= 2000, label + ': source translation exceeds browser prompt limit')
    nav_pos = text.find('<a id="find-the-right-prompt">')
    gallery_pos = text.find('<a id="featured-prompts">')
    workflow_pos = text.find('<a id="seaimagine-browser-workflow">')
    community_pos = text.find('<a id="learn-from-official-and-community-examples">')
    require(0 <= nav_pos < gallery_pos < community_pos < workflow_pos, label + ': broken reader journey')
    require(text.count('assets/seaimagine-interface.jpg') == 0, label + ': duplicated product tutorial')
    gallery = text[gallery_pos:community_pos]
    require(len(re.findall(r'```text\n', gallery)) == 8, label + ': expected eight complete gallery prompts')
    require(all('prompts/' + x in text[:gallery_pos] for x in ['01-ads-and-products.md', '02-cinematic-storytelling.md', '03-social-ugc.md', '04-characters-and-references.md', '05-editing-and-extension.md']), label + ': categories not before gallery')
    require(gallery.find('case-sea-glass-bottle') < gallery.find('case-blue-route') < gallery.find('case-honey-loaf'), label + ': opening lacks topic variety')
    require(text.count('[TXT]') == 8, label + ': missing text exports')
    for case in data['cases']:
        require((ROOT / 'prompts/text' / item['locale'] / (case['id'] + '.txt')).read_text().rstrip('\n') == case['prompt'], label + ': source TXT mismatch')
    require('height="180"' not in text and '### ' + data['preview_title'] not in text, label + ': removed visual overview returned')
    explicit_ids = re.findall(r'<a id="([^"]+)"', text)
    require(len(explicit_ids) == len(set(explicit_ids)), label + ': duplicate explicit anchors')
require(sum(len(re.findall(r'^## \d+\.', p.read_text(), re.M)) for p in (ROOT / 'prompts').glob('0[1-5]-*.md')) == 30, 'Expected 30 inherited category recipes')
new_files = ['07-satisfying-materials', '08-spaces-and-transformations', '09-miniature-and-surreal', '10-fashion-and-performance']
new_prompts = []
for slug in new_files:
    content = (ROOT / 'prompts' / (slug + '.md')).read_text()
    bodies = re.findall(r'```text\n(.*?)\n```', content, re.S)
    require(len(bodies) == 6, slug + ': expected six original recipes')
    require(len(re.findall(r'\*\*Output:\*\* (?:5|10)s · (?:16:9|9:16) · 720p', content)) == 6, slug + ': unsupported new brief settings')
    for i, body in enumerate(bodies, 1):
        require(len(body) <= 2000, slug + ': prompt too long')
        require((ROOT / 'prompts/text/en-US' / (slug + '-' + str(i) + '.txt')).read_text() == body + '\n', slug + ': TXT mismatch')
    new_prompts.extend(bodies)
require(len(set(new_prompts)) == 24, 'Repeated new original prompt')
require((ROOT / 'docs/PROMPT_INDEX.md').read_text().count('[TXT]') == 62, 'Complete index must link all 62 prompts')
exercise_text = (ROOT / 'prompts/06-community-exercises.md').read_text()
require(len(re.findall(r'^## \d+\.', exercise_text, re.M)) == 3, 'Expected three new exercises')
exercise_prompts = re.findall(r'```text\n(.*?)\n```', exercise_text, re.S)
require(exercise_prompts == [case['prompt'] for case in master['cases']], 'English exercise prompts differ from canonical en-US.json')
require('Copyright (c) 2026 Flaq AI' in (ROOT / 'LICENSE').read_text(), 'Missing upstream copyright')
assets = json.loads((ROOT / 'data/assets.json').read_text())
require(len({asset['file'] for asset in assets}) == len(assets), 'Duplicate asset record')
require({case[1] for case in fixed_cases} | {'assets/seaimagine-interface.jpg'} <= {asset['file'] for asset in assets}, 'Missing provenance records for new starting frames or interface screenshot')
for asset in assets:
    p = ROOT / asset['file']
    require(p.exists() and hashlib.sha256(p.read_bytes()).hexdigest() == asset['sha256'], 'Changed or missing asset: ' + asset['file'])
    require(bool(asset.get('origin', '').strip()), 'Missing asset origin: ' + asset['file'])
result = subprocess.run([sys.executable, str(ROOT / 'scripts/build.py'), '--check'], capture_output=True, text=True)
require(result.returncode == 0, result.stdout.strip() + '\n' + result.stderr.strip())
if errors:
    raise SystemExit('\n'.join(errors))
print('PASS: local Markdown/HTML links, 15 complete localized homepages, 62 English recipes, synchronized prompts, provenance and assets')
