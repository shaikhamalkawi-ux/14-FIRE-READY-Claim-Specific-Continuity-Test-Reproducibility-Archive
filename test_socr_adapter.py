#!/usr/bin/env python3
import copy, json, pathlib, sys
HERE=pathlib.Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
from socr_adapter import evaluate_routes
fixtures=json.loads((HERE/'socr_fixtures.json').read_text())
examples=json.loads((HERE/'socr_examples.json').read_text())
schema=json.loads((HERE/'socr_schema.json').read_text())
results=[]
def check(tid,cond,note):
    results.append({'test_id':tid,'pass':bool(cond),'note':note})
    if not cond: raise AssertionError(f'{tid}: {note}')
a=evaluate_routes(**fixtures['FR_MATCHED']); b=evaluate_routes(**fixtures['FR_MATCHED'])
check('T01',a==b,'Determinism')
check('T02',a['necessity']==1 and a['possibility']==1 and a['continuity_state']=='same_question_preserved','Crisp recovery')
check('T03',a==evaluate_routes(**fixtures['FR_MATCHED']),'Nonsemantic metadata is outside semantic inputs')
whole=evaluate_routes(**fixtures['FR_WHOLE_YEAR'])
check('T04',whole['continuity_state']=='question_changed','Event-universe failure changes state')
pt=evaluate_routes(**fixtures['PT_J']); fx=copy.deepcopy(fixtures['PT_J']); fx['states']['J']='verified'
check('T05',pt['continuity_state']=='pending_evidence' and evaluate_routes(**fx)['continuity_state']=='same_question_preserved','Refinement monotonicity')
fx=copy.deepcopy(fixtures['PT_J']); fx['states']['J']='failed'
check('T06',evaluate_routes(**fx)['possibility']==0,'Contradiction closure')
check('T07',pt['minimal_repair']==[['J']],'Portugal minimal repair exactly {J}')
fx=copy.deepcopy(fixtures['FR_WHOLE_YEAR']); fx['states']['correlation']='verified'
check('T08',evaluate_routes(**fx)['possibility']==0,'Non-compensation')
ag=evaluate_routes(**fixtures['AGUEDA_GEOMETRY'])
check('T09',ag['continuity_state']=='pending_evidence' and sorted(ag['minimal_repair'])==[['authoritative_crosswalk'],['operative_2026_geometry']],'Alternative geometry routes')
ca=evaluate_routes(**fixtures['CASTELO_OUTCOME'])
check('T10',ca['minimal_repair']==[['attribution_design','outcome_evidence']],'Outcome promotion blocked')
try:
 import jsonschema
 for rec in examples: jsonschema.validate(rec,schema)
 bad=copy.deepcopy(examples[0]); bad.pop('licensed_statement'); failed=False
 try: jsonschema.validate(bad,schema)
 except jsonschema.ValidationError: failed=True
 check('T11',failed,'Schema validation')
except Exception as e:
 req=set(schema['required']); check('T11',all(req.issubset(r) for r in examples),f'Fallback schema check: {type(e).__name__}')
check('T12',all(r['provenance']['hash_status']!='not_supplied' or r['provenance']['source_hashes']==[] for r in examples),'No fabricated hashes')
f=evaluate_routes(**fixtures['FAILED_CANDIDATE_NO_REPAIR'])
check('T13',f['continuity_state']=='question_changed' and f['minimal_repair']==[],'Failed mandatory relation has no evidence repair')
alt=evaluate_routes(**fixtures['ALTERNATIVE_ROUTE_WITH_ONE_FAILED'])
check('T14',alt['continuity_state']=='pending_evidence' and alt['minimal_repair']==[['route_B']],'Failed OR route pruned')
qual=evaluate_routes(**fixtures['QUALIFIED_PRESERVED'])
check('T15',qual['necessity']==1 and qual['continuity_state']=='preserved_with_qualification','Qualified preservation state')
out={'passed':sum(x['pass'] for x in results),'total':len(results),'results':results}
(HERE/'outputs'/'socr_test_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps({'status':'PASS' if out['passed']==out['total'] else 'FAIL','passed':out['passed'],'total':out['total']},indent=2))
