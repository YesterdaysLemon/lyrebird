"""Import selected, audited manuscripts. No project directories are modified."""
import hashlib
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LLM = Path('C:/w/kv-policy-20260922')
LEARN = Path('C:/Users/Yeste/Project/learn2design')
GRAPH = Path('C:/Users/Yeste/OneDrive/Documents/open-graph-theory-with-prize')
LLM_SHA = 'eebfa80d060612c1b832b26938e09edef70c484e'
LLM_PUBLIC_SHA = 'da616c39ba57eeb4d076b36ef320d603b3e9a258'
LEARN_SHA = '1747af93d167e15720cd66b5d1f662eaa48ea299'
GRAPH_SHA = '3981294564c183fee1454c5ddd2df627aff095d9'

items = [
    dict(slug='learning-what-to-keep', title='Learning what to keep under a real KV-cache budget', date='2026-09-22',
         topic='Machine learning', type='Pilot study', project='LLM Research', version='1.0',
         summary='A learned cache policy, an 8 GiB GPU, and a strict memory budget. A completed pilot finds no consistent benefit from compression exposure—and an important evaluation confound.',
         evidence='33 primary conditions · 24 paired tasks', limit='One small synthetic task family. Cache storage shrinks, total GPU savings are small, and answer format confounds retrieval scores.',
         repo='llm-research', sha=LLM_SHA, root=LLM, path='experiments/E010-kv-policy-compression/report.md',
         editionNote='The completed primary pilot and separately frozen post-primary diagnostic are reported together. All primary conditions and the failed initial implementation smoke are retained. The diagnostic does not replace the original endpoint.'),
    dict(slug='voice-without-a-prescribed-self', title='A voice without a prescribed self', date='2026-09-21',
         topic='Model behavior', type='Research note', project='LLM Research', version='1.1',
         summary='Six fine-tuning runs test whether removing literal self-claims changes a model’s conversational voice. A matched control makes the causal story more modest.',
         evidence='6 completed runs · 2 paired seeds', limit='Single-agent coding; no clear filter-specific effect and no inference about subjective experience.',
         repo='llm-research', sha=LLM_SHA, root=LLM, path='experiments/E009-interiority-ablation/cloud/report/paper.md',
         editionNote='The research text and figures are preserved. This public edition replaces personal account balances with aggregate observed study cost and replaces a local archive path with a preservation statement.'),
    dict(slug='heart-wall-sampling', title='One prompt, 550 heart walls', date='2026-09-15',
         topic='Model behavior', type='Research note', project='LLM Research', version='1.0',
         summary='Across 550 fresh coding-agent sessions, every wall was a red rectangle. Requested effort changed size without a monotonic pattern.',
         evidence='550 registered sessions · 11 conditions', limit='One exact prompt and two installed agent products. These are product-level observations, not bare-model comparisons.',
         repo='llm-research', sha=LLM_SHA, root=LLM, path='experiments/E006-heart-wall-agent-sampling/report.md'),
    dict(slug='fixed-rate-optimization', title='Larger steps in detector optimization', date='2026-09-05',
         topic='Optimization', type='Research note', project='Learn2Design', version='1.0',
         summary='A fourfold increase in Adam learning rates improves feasible loss on two fresh detector topologies in a fixed 600-second diagnostic.',
         evidence='4 runs · 2 topology pairs · replay checked', limit='One optimizer seed per topology; no significance claim, competition submission, or hidden-score estimate.',
         repo='learn2design', sha=LEARN_SHA, root=LEARN, path='research/2026-09-05-fixed-rate-uifo-results.md'),
    dict(slug='ghz-closure', title='GHZ tensors in the closure of matching tensors', date='2026-09-01',
         topic='Mathematics', type='Mathematical note', project='Krenn–Gu Research', version='1.1',
         summary='An explicit truncation construction places ternary GHZ tensors in the closure of the matching-tensor image at every even order, limiting a class of proof strategies.',
         evidence='Written proof · exact and numerical checks', limit='A closure theorem. It does not solve the Krenn–Gu conjecture; the general nonattainment consequence remains conditional.',
         repo='krenn-gu-research', sha=GRAPH_SHA, root=GRAPH, path='claims/arbitrary-order/GHZ_CLOSURE_MATCHING_POLYTOPE_FACE_ASYMPTOTIC_REALIZABILITY_THEOREM.md',
         editionNote='This edition explicitly requires a nonnegative continuous loss in Corollary D, as needed for its infimum claim, and limits the proof-route conclusion to closed tensor-only separators. Supporting programs were rerun for this release. These edits do not claim new independent peer review.'),
    dict(slug='relational-layer-geometry', title='Relational layer geometry improves compositional transfer under a capability ceiling', date='2026-08-19',
         topic='Machine learning', type='Preprint', project='LLM Research', version='1.0',
         summary='Relational distillation improves held-out composition on a synthetic affine task. Strong controls reveal both the transfer gain and a sharp capability ceiling.',
         evidence='Paired-seed study · controls and follow-ups', limit='Synthetic affine composition. No general language-model capability, hardware efficiency, or energy-saving claim.',
         repo='llm-research', sha=LLM_SHA, root=LLM, path='paper/preprint.md'),
]

def main():
    (ROOT/'content').mkdir(exist_ok=True)
    provenance=[]
    for item in items:
        src=item['root']/item['path']
        raw=src.read_bytes()
        text=raw.decode('utf-8-sig').replace('\r\n','\n').replace('\r','\n')
        slug=item['slug']
        asset=ROOT/'public'/'papers'/slug
        asset.mkdir(parents=True,exist_ok=True)
        if slug=='learning-what-to-keep':
            shutil.copytree(src.parent/'figures',asset/'figures',dirs_exist_ok=True)
            text=text.replace('](figures/',f'](/papers/{slug}/figures/')
        elif slug=='voice-without-a-prescribed-self':
            text=re.sub(r'Starting credit was.*?billing may settle later\.', 'The observed cloud-credit decrease was approximately $10.14, below the $22 allocation. Both pods and the temporary volume were deleted, with zero hourly spend at the recorded final check. This is an observed balance change rather than a settled invoice.', text, flags=re.S)
            text=text.replace('Large artifacts live at D:/Interiority-V1/cloud/retrieved.', 'Large artifacts are preserved in the project owner’s verified local archive; they are not served by this site.')
            shutil.copytree(src.parent/'figures',asset/'figures',dirs_exist_ok=True)
            text=text.replace('](figures/',f'](/papers/{slug}/figures/')
            text=text.replace('<!-- pagebreak -->','')
        elif slug=='ghz-closure':
            text=text.replace('every\ncontinuous loss', 'every\nnonnegative continuous loss')
            text=text.replace('Every valid proof must use\nthe exact fibre', 'A proof using the excluded closed tensor-only routes must instead use\nadditional information, such as the exact fibre')
            text=text.replace('**Every proof must be fibre-exact.**', '**Closed tensor-only separators are insufficient.**')
            text=text.replace('A proof cannot consist of invariants of `T_W`; it must\n   derive structure of `W` from the exact equation', 'A proof cannot consist solely of closed conditions containing the whole image of `T_W`; an available alternative is to\n   derive structure of `W` from the exact equation')
        elif slug=='relational-layer-geometry':
            shutil.copyfile(LLM/'output/pdf/relational_activation_distillation_preprint.pdf',asset/'paper.pdf')
            # This manuscript refers to its figure directory locally.
            figures=LLM/'paper/figures'
            if figures.exists():shutil.copytree(figures,asset/'figures',dirs_exist_ok=True)
            text=text.replace('](figures/',f'](/papers/{slug}/figures/')
            generated=LLM/'paper/generated'
            if generated.exists():
                (asset/'generated').mkdir(exist_ok=True)
                for figure in generated.glob('*.png'):shutil.copyfile(figure,asset/'generated'/figure.name)
            text=text.replace('](generated/',f'](/papers/{slug}/generated/')
        (ROOT/'content'/f'{slug}.md').write_text(text,encoding='utf-8',newline='\n')
        release_sha=LLM_PUBLIC_SHA if item['repo']=='llm-research' else item['sha']
        original_sha='c855049' if slug=='learning-what-to-keep' else item['sha']
        provenance.append({'slug':slug,'repository':item['repo'],'original_development_commit':original_sha,'public_source_commit':release_sha,'source_path':item['path'],'original_source_sha256':hashlib.sha256(raw).hexdigest(),'published_markdown_sha256':hashlib.sha256(text.encode()).hexdigest(),'edition_note':item.get('editionNote','Source text preserved; title and presentation curated for the library.')})
        item['source']=f"https://github.com/YesterdaysLemon/{item['repo']}/blob/{release_sha}/{item['path']}"
        parent=str(Path(item['path']).parent).replace('\\','/')
        item['sourceBase']=f"https://github.com/YesterdaysLemon/{item['repo']}/blob/{release_sha}/{parent}/"
    cleaned=[{k:v for k,v in i.items() if k not in ('root','path','repo','sha')} for i in items]
    (ROOT/'content/papers.json').write_text(json.dumps(cleaned,indent=2,ensure_ascii=False),encoding='utf-8')
    (ROOT/'content/provenance.json').write_text(json.dumps(provenance,indent=2,ensure_ascii=False),encoding='utf-8')
    print('Imported',len(items),'audited manuscripts')

if __name__=='__main__':main()
