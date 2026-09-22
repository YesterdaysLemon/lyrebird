"""Export the inspected four-run synthetic optimizer evidence, excluding rentals."""
from pathlib import Path
import hashlib,json,shutil,zipfile
root=Path(__file__).resolve().parents[1]
project=Path('C:/Users/Yeste/Project/learn2design')
results=project/'artifacts/generated/rate-uifo-20260905-v3-600-host2/results'
dest=root/'public/papers/fixed-rate-optimization';dest.mkdir(parents=True,exist_ok=True)
evidence=root/'evidence/learn2design';(evidence/'research').mkdir(parents=True,exist_ok=True)
for name in ['2026-09-05-fixed-rate-uifo-results.md','2026-09-05-fixed-rate-uifo-plan.md']:
    shutil.copyfile(project/'research'/name,evidence/'research'/name)
with zipfile.ZipFile(dest/'evidence.zip','w',compression=zipfile.ZIP_DEFLATED) as z:
    files=[results/name for name in ['plan.json','analysis.json','budget-ladder.json','final-comparison.csv','final-data-summary.json']]
    files += [results/f'{i}-{arm}.{ext}' for i in range(2) for arm in ['baseline','rate_4x'] for ext in ['json','npz']]
    for p in files:z.write(p,'results/'+p.name)
    bundle=project/'artifacts/generated/rate-uifo-20260905-v3-600/source-bundle.zip'
    with zipfile.ZipFile(bundle) as source:
        members=source.namelist()
        assert len(members)==9
    z.write(bundle,'source-bundle.zip')
    manifest={p.name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
    z.writestr('MANIFEST.json',json.dumps(manifest,indent=2))
archive=dest/'evidence.zip';digest=hashlib.sha256(archive.read_bytes()).hexdigest()
(evidence/'README.md').write_text(f'''# Learn2Design: fixed-rate diagnostic evidence

This public snapshot accompanies “Larger steps in detector optimization.”
Original development commit: `1747af93d167e15720cd66b5d1f662eaa48ea299`.
The original project is https://github.com/YesterdaysLemon/learn2design.

- [Result and limits](research/2026-09-05-fixed-rate-uifo-results.md)
- [Frozen plan](research/2026-09-05-fixed-rate-uifo-plan.md)
- [Download the public evidence archive](https://lyrebird.alirezaafshan.com/papers/fixed-rate-optimization/evidence.zip)

Archive size: {archive.stat().st_size:,} bytes. SHA-256: `{digest}`.

The archive contains four generated-topology NPZ histories and JSON records,
the frozen plan, audited analysis, budget prefixes, summary, paired CSV, and
the original nine-member source bundle. It excludes rental/provider records
and any official competition dataset. The source bundle includes the runner,
independent history auditor, unchanged optimizer source, and dependencies.
Its own source provenance is recorded in the frozen plan. The history auditor
uses a restricted NumPy decoder; do not load arbitrary pickle files unsafely.

Fresh replay on September 22, 2026 verified all four histories and reproduced
the mean paired feasible-loss difference -1.6138125667514436. This remains a
two-topology, one-seed diagnostic and is not a public leaderboard score.
Source software retains its original project license and dependency licenses.
''',encoding='utf-8',newline='\n')
print('Published evidence:',archive.stat().st_size,'bytes;',digest)
