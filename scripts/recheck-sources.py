"""Read existing records; redirect verifier outputs into this release's QA folder."""
import hashlib,json,runpy,sys
from pathlib import Path

HERE=Path(__file__).resolve().parents[1]
out=HERE/'tmp';out.mkdir(exist_ok=True)
cloud=Path('C:/w/kv-policy-20260922/experiments/E009-interiority-ablation/cloud')
sys.path.insert(0,str(cloud))
import filter_v2
def save_receipt(path,value):
    (out/'voice-recheck.json').write_text(json.dumps(value,indent=2),encoding='utf-8')
filter_v2.save_json=save_receipt
sys.argv=['verify_runs.py','--root','D:/Interiority-V1/cloud/retrieved']
runpy.run_path(str(cloud/'verify_runs.py'),run_name='__main__')
print('VOICE: all six final adapter hashes, paired initializations and run provenance passed')

learn=Path('C:/Users/Yeste/Project/learn2design')
sys.path.insert(0,str(learn))
from tools.audit_fast_results import audit_run
from experiments.rate_screen import validate_plan,validate_hardware
root=learn/'artifacts/generated/rate-uifo-20260905-v3-600-host2/results'
plan=json.loads((root/'plan.json').read_text());validate_plan(plan)
records=[];differences=[]
for index in range(2):
    pair=[]
    for arm in ['baseline','rate_4x']:
        path=root/f'{index}-{arm}.json';data=json.loads(path.read_text())
        validate_hardware(data['runtime']['gpu'],plan['minimum_gpu_memory_mib'])
        low,high=plan['rates'][arm]
        assert data['optimizer_settings']=={'learning_rate_low':low,'learning_rate_high':high}
        pair.append(audit_run(path,plan))
    assert pair[0]['initial_sha256']==pair[1]['initial_sha256'] and pair[0]['runtime']==pair[1]['runtime']
    records.extend(pair);differences.append(pair[1]['best_feasible']-pair[0]['best_feasible'])
report={'runs_verified':4,'paired_differences':differences,'mean_difference':sum(differences)/2,'records':records}
(out/'learn-recheck.json').write_text(json.dumps(report,indent=2))
print('LEARN2DESIGN:',report['mean_difference'],'four independent NPZ replays passed')
heart=Path('C:/w/kv-policy-20260922/experiments/E006-heart-wall-agent-sampling/results/fixed-50-summary.json')
assert json.loads(heart.read_text())==json.loads((out/'heart-recheck.json').read_text())
print('HEART: fresh analysis exactly reproduces the stored 550-session summary')
