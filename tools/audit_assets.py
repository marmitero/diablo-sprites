#!/usr/bin/env python3
"""Measure originals without inferring semantic sprite frames."""
import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
# Known large sheets in this trusted, local collection exceed Pillow's warning limit.
# Retain a finite bound above the largest original; never apply this to arbitrary uploads.
Image.MAX_IMAGE_PIXELS = 160_000_000

def audit():
    images, archives = [], []
    for path in sorted((ROOT / 'sprites').rglob('*')):
        if not path.is_file():
            continue
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        common = {'path': path.relative_to(ROOT).as_posix(),
                  'bytes': path.stat().st_size, 'sha256': digest}
        if path.suffix.lower() in ('.png', '.gif'):
            with Image.open(path) as im:
                im.load()
                images.append(dict(common, width=im.width, height=im.height,
                                   mode=im.mode, file_frames=im.n_frames if hasattr(im, 'n_frames') else 1,
                                   semantic_frame_count=None,
                                   alpha_channel='A' in im.getbands(),
                                   transparency_metadata='transparency' in im.info))
        elif path.suffix.lower() == '.zip':
            import zipfile
            with zipfile.ZipFile(path) as archive:
                archives.append(dict(common, entries=[{'path': i.filename, 'bytes': i.file_size,
                                                       'directory': i.is_dir()} for i in archive.infolist()]))
        else:
            raise ValueError(f'Unclassified original: {path}')
    return {'schema_version': 1, 'image_count': len(images),
            'format_counts': dict(Counter(Path(i['path']).suffix.lower() for i in images)),
            'group_counts': dict(Counter(i['path'].split('/')[1] for i in images)),
            'images': images, 'archives': archives}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    if output.is_relative_to(ROOT / 'sprites'):
        parser.error('Output must not overwrite the original sprites tree')
    result = audit()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['image_count', 'format_counts', 'group_counts']}))
