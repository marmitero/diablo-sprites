#!/usr/bin/env python3
"""Extract only reviewed example blocks, with artificial preview timing."""
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]

def extract(output):
    manifest = json.loads((ROOT / 'examples/layouts.json').read_text())
    results = []
    for layout in manifest['layouts']:
        source = ROOT / layout['source_path']
        with source.open('rb') as stream:
            if hashlib.file_digest(stream, 'sha256').hexdigest() != layout['source_sha256']:
                raise ValueError(f'Changed source: {source}')
        with Image.open(source) as opened:
            im = opened.convert('RGBA')
        groups = defaultdict(list)
        for entry in layout['frames']:
            x, y, w, h = entry['rect']
            if not (w > 0 and h > 0 and x >= 0 and y >= 0 and x+w <= im.width and y+h <= im.height):
                raise ValueError(f'Invalid rectangle: {entry}')
            crop = im.crop((x, y, x+w, y+h))
            keys = {tuple(k) for k in layout['color_key']}
            data = crop.get_flattened_data() if hasattr(crop, "get_flattened_data") else crop.getdata()
            pixels = [(red, green, blue, 0 if (red, green, blue) in keys else alpha)
                      for red, green, blue, alpha in data]
            crop.putdata(pixels)
            if crop.getbbox() is None:
                raise ValueError(f'Unexpected empty example: {layout["action"]} {entry}')
            # No independent trimming or recentering; preserve cell geometry.
            folder = output / source.stem / layout['action'] / entry['view']
            folder.mkdir(parents=True, exist_ok=True)
            crop.save(folder / f'{entry["index"]:04d}.png')
            groups[entry['view']].append((entry['index'], crop))
        for view, frames in groups.items():
            ordered = [im for _, im in sorted(frames)]
            # A neutral, opaque preview avoids GIF partial-alpha/palette artefacts.
            previews = []
            for frame in ordered:
                bg = Image.new('RGBA', frame.size, (48, 48, 48, 255))
                bg.alpha_composite(frame)
                previews.append(bg.convert('RGB'))
            previews[0].save(output / source.stem / layout['action'] / view / 'study-preview.gif',
                             save_all=True, append_images=previews[1:],
                             duration=layout['preview_duration_ms'], loop=0, disposal=2)
        results.append({'source': layout['source_path'], 'action': layout['action'],
                        'cells': len(layout['frames']), 'views': len(groups),
                        'timing': '100ms for study; native timing unknown'})
    (output / 'extraction-report.json').write_text(json.dumps(results, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(results, ensure_ascii=False))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT / 'sprites') or output == ROOT:
        parser.error('Use a separate output directory, never original sprites or repository root')
    extract(output)
