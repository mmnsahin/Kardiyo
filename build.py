"""Builds index.html from data/. Run: python3 build.py"""
import json, base64, pathlib
root = pathlib.Path(__file__).parent
rows = json.loads((root/'data/rows.json').read_text(encoding='utf-8'))
sections = json.loads((root/'data/sections.json').read_text(encoding='utf-8'))
images = {}
for r in rows:
    for b in r['blocks']:
        if b['type'] == 'image':
            images[b['src']] = 'data:image/jpeg;base64,' + base64.b64encode((root/'data'/b['src']).read_bytes()).decode()
data = json.dumps({'rows': rows, 'sections': sections, 'images': images}, ensure_ascii=False).replace('</', '<\\/')
(root/'index.html').write_text((root/'template.html').read_text(encoding='utf-8').replace('__DATA__', data), encoding='utf-8')
print('index.html yazıldı:', len(rows), 'soru,', len(images), 'görsel')
