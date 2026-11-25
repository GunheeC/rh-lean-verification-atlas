#!/usr/bin/env python3
"""Check the packaged page inventory; optionally compare every pixel to the pinned local PDF."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile


def sha(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    parser.add_argument('--pdf',type=Path,help='Optional local PDF for blueprint v13, v13a, v13b or v13c. Re-rendering uses macOS PDFKit, Swift and Pillow.')
    args=parser.parse_args(); root=args.root
    records=json.loads((root/'data/notes_starters.json').read_text())['starters']
    editions=json.loads((root/'data/editions.json').read_text())['editions']
    pages={}
    for track,r in records.items():
        if r['edition']!='blueprint_v13' or len(r['printed_pages'])!=len(r['pdf_pages']):
            raise ValueError('Inconsistent packet: '+track)
        if set(map(str,r['printed_pages']))!=set(r['page_image_hashes']):
            raise ValueError('Page register differs from packet: '+track)
        for number,pdf_page in zip(r['printed_pages'],r['pdf_pages']):
            file=root/'notes'/track/'pages'/f'{number}.webp'
            if sha(file)!=r['page_image_hashes'][str(number)]:
                raise ValueError('Changed image: '+str(file))
            pages[file]=pdf_page
    if set((root/'notes').glob('*/pages/*'))!=set(pages):
        raise ValueError('Unregistered image in page packet')
    print(f'{len(pages)} images match the packet registers; {len(set(pages.values()))} distinct PDF pages.')
    if not args.pdf:
        return
    from PIL import Image,ImageChops
    digest = sha(args.pdf)
    revised = next((editions[k] for k in ('blueprint_v13a', 'blueprint_v13b', 'blueprint_v13c')
                    if digest == editions[k]['sha256']), None)
    if revised:
        from edition_links import blueprint_page
        pages = {file: blueprint_page(revised, page) for file, page in pages.items()}
    elif digest != editions['blueprint_v13']['sha256']:
        raise ValueError('PDF differs from all registered blueprint editions')
    with tempfile.TemporaryDirectory() as temporary:
        tmp=Path(temporary);exe=tmp/'pages'
        subprocess.run(['swiftc','-module-cache-path',str(tmp/'swift-cache'),str(root/'scripts/extract_pages.swift'),'-o',str(exe)],check=True)
        subprocess.run([str(exe),str(args.pdf),str(tmp),*map(str,sorted(set(pages.values())))],check=True)
        for image,pdf_page in pages.items():
            with Image.open(image) as saved,Image.open(tmp/f'p{pdf_page}.png') as rendered:
                a=saved.convert('RGB');b=rendered.convert('RGB')
                if a.size!=b.size or ImageChops.difference(a,b).getbbox():
                    raise ValueError('Decoded pixels differ: '+str(image))
    print('All decoded RGB pixels agree with a fresh rendering of the registered PDF.')


if __name__=='__main__':
    main()
