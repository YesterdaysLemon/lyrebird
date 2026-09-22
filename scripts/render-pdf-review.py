from pathlib import Path
import json
import pypdfium2 as pdfium
from PIL import Image,ImageOps,ImageDraw
from pypdf import PdfReader

root=Path(__file__).resolve().parents[1]
out=root/'tmp/pdfs';out.mkdir(parents=True,exist_ok=True)
reports=[]
for path in sorted((root/'public/papers').glob('*/paper.pdf')):
    slug=path.parent.name
    pdf=pdfium.PdfDocument(path)
    reader=PdfReader(path)
    thumbs=[]
    for n,page in enumerate(pdf):
        image=page.render(scale=1.1).to_pil().convert('RGB')
        image.save(out/f'{slug}-{n+1:02}.png')
        image.thumbnail((310,440))
        tile=Image.new('RGB',(330,468),'#e9e9e9');tile.paste(image,((330-image.width)//2,10))
        ImageDraw.Draw(tile).text((12,450),f'{slug} / {n+1}',fill='black')
        thumbs.append(tile)
    for at in range(0,len(thumbs),9):
        group=thumbs[at:at+9]
        sheet=Image.new('RGB',(990,468*((len(group)+2)//3)),'#ccc')
        for j,im in enumerate(group):sheet.paste(im,((j%3)*330,(j//3)*468))
        sheet.save(out/f'{slug}-sheet-{at//9+1}.png')
    counts=[len(p.extract_text() or '') for p in reader.pages]
    assert all(n>80 for n in counts),(slug,'empty page',counts)
    reports.append({'slug':slug,'pages':len(pdf),'page_characters':counts,'bytes':path.stat().st_size})
(out/'review.json').write_text(json.dumps(reports,indent=2))
print(json.dumps(reports,indent=2))
