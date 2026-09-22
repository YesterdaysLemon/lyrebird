"""Prepare the selected public evidence branch, preserving the private archive."""
import hashlib,json,re,shutil
from pathlib import Path
site=Path(__file__).resolve().parents[1]
root=Path('C:/w/lyrebird-papers-source')
cloud=root/'experiments/E009-interiority-ablation/cloud'
paper=(cloud/'report/paper.md').read_text(encoding='utf-8')
paper=re.sub(r'Starting credit was.*?billing may settle later\.', 'The observed cloud-credit decrease was approximately $10.14, below the $22 allocation. Both pods and the temporary volume were deleted, with zero hourly spend at the final recorded check. Personal account balance snapshots are omitted from this public edition; the original verified archive is preserved locally.',paper,flags=re.S)
(cloud/'report/paper.md').write_text(paper,encoding='utf-8')
completion=json.loads((cloud/'report/completion.json').read_text())
for key in ['initial_credit_usd','observed_remaining_credit_usd','previous_balance_snapshots','pods','network_volume']:
    completion.pop(key,None)
completion['public_edition_note']='Personal balance snapshots and deleted infrastructure identifiers omitted; the original private receipt is preserved.'
(cloud/'report/completion.json').write_text(json.dumps(completion,indent=2),encoding='utf-8')
config=json.loads((cloud/'config.json').read_text())
config.pop('initial_balance_usd',None)
(cloud/'config.json').write_text(json.dumps(config,indent=2),encoding='utf-8')
protocol=(cloud/'protocol.md').read_text().replace('from the observed $27.6401769675 balance, with','from the authorized study budget, with')
(cloud/'protocol.md').write_text(protocol,encoding='utf-8')
readme=(cloud/'report/README.md').read_text()
readme=readme.replace('[Read the five-page paper](../../../../output/pdf/e009-voice-study.pdf)','[Read the public paper](https://lyrebird.alirezaafshan.com/papers/voice-without-a-prescribed-self/)')
readme=readme.replace('Exact balance snapshot and verified teardown','Aggregate observed cost and verified teardown')
readme=re.sub(r'Starting credit:.*?always-on service was used\.', 'Observed study cost was approximately $10.14, with zero hourly spend after verified teardown. Personal account balances are omitted from this public edition. Billing may settle later; this is not a final invoice. No model weights or always-on inference service are published.',readme,flags=re.S)
(cloud/'report/README.md').write_text(readme,encoding='utf-8')
manifest=json.loads((cloud/'report/release-manifest.json').read_text())
manifest['public_edition_note']='This is the original private-release provenance ledger. Personal account balance snapshots and infrastructure identifiers were removed for the public source edition, so modified/omitted entries do not validate this public edition. See PUBLICATION.md and public-release-manifest.json.'
(cloud/'report/release-manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
(root/'PUBLICATION.md').write_text('''# Lyrebird research source release

This branch publishes selected E006, E009, and E010 evidence for the Lyrebird
library. It leaves the development checkout and its unrelated experiments
untouched. E006/E009 were copied from local development commit
`eebfa80d060612c1b832b26938e09edef70c484e`.

E009's public edition omits personal cloud account balances and deleted
infrastructure identifiers. Its scientific results, evaluation outputs, paired
initialization records, and training code are preserved. The original private
release ledger is retained as historical provenance and explicitly marked as
such. No model weights or full training corpus are distributed here.

E010 was frozen in local commits before its fixed run; its recorded local commit
IDs and source hashes identify that protocol. This public branch is an evidence
release after completion, not a claim of external preregistration. The fixed
run is a pilot, not a competitive benchmark or general capability result.

Papers and public editions: https://lyrebird.alirezaafshan.com/
''',encoding='utf-8')
print('Prepared public source edition; original records preserved')
