#!/usr/bin/env python3
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from socr_adapter import evaluate_routes
def canon(rs): return sorted(tuple(sorted(x)) for x in rs)
registry=json.loads((HERE/'socr_rule_registry.json').read_text()); records=json.loads((HERE/'socr_examples.json').read_text())
vals=[]
for rec in records:
 r=registry['claims'][rec['claim_id']]; d=evaluate_routes(r['routes'],r['states'],r.get('qualified',False)); mp=r.get('record_role_map',{})
 mapped=[[mp.get(role,role) for role in repair] for repair in d['minimal_repair']]
 p=rec['pcae']; checks={'state':rec['continuity_state']==d['continuity_state'],'N':p['necessity']==d['necessity'],'Pi':p['possibility']==d['possibility'],'repair':canon(rec['minimal_repair'])==canon(mapped)}
 vals.append({'claim_id':rec['claim_id'],'checks':checks,'pass':all(checks.values())})
report={'records_checked':len(vals),'records_passed':sum(v['pass'] for v in vals),'all_pass':all(v['pass'] for v in vals),'validation':vals}
(HERE/'outputs'/'rule_to_record_validation.json').write_text(json.dumps(report,indent=2))
print(json.dumps({'status':'PASS' if report['all_pass'] else 'FAIL','records_passed':report['records_passed'],'records_checked':report['records_checked']},indent=2))
if not report['all_pass']: raise SystemExit(1)
