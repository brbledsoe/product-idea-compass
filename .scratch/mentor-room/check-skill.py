"""Meaningful structural checks for the room; fixture observations are fictional."""
import copy
import csv
import importlib.util
import json
import re
import tempfile
from pathlib import Path
from urllib.parse import unquote

root = Path(__file__).resolve().parents[2]
skill = root / '.agents/skills/mentor-room'
spec = importlib.util.spec_from_file_location('mentor_case', skill/'scripts/case.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
results = []

catalog = module.library('catalog.json')['resources']
with (root/'research/mentor-room/resources.csv').open(encoding='utf-8-sig', newline='') as f:
    original = list(csv.DictReader(f))
assert len(catalog) == len(original) == 49
for a, b in zip(catalog, original):
    assert a['id'] == int(b['Recommended_Order'])
    assert a['author'] == b['Person_or_Author']
    assert a['title'] == b['Resource_Title']
    assert a['primary_url'] == b['Primary_Link']
results.append('All49 catalog identities match the unchanged source inventory')

links = []
for path in skill.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
        if re.match(r'^\w+://', target):
            continue
        local = unquote(target.split('#')[0])
        if local:
            assert (path.parent/local).resolve().is_file(), (path, target)
        links.append((str(path.relative_to(skill)), target))
for row in catalog:
    if row['method_reference']:
        assert (root/'research/mentor-room'/row['method_reference']).is_file()
results.append(f'{len(links)} skill Markdown links and catalog method references resolve')

fixture_root = Path(tempfile.mkdtemp(prefix='mentor-room-structural-')).resolve()
assert fixture_root.is_relative_to(Path(tempfile.gettempdir()).resolve())
case_dir = fixture_root/'fictional-case'
module.initialize(case_dir, 'Fictional checker case')
fresh = json.loads((case_dir/'case.json').read_text(encoding='utf-8'))

def save(value):
    (case_dir/'case.json').write_text(json.dumps(value), encoding='utf-8')

assert module.check(case_dir)['valid']
assert module.check(case_dir)['core_status'] == 'incomplete'
assert len(module.check(case_dir)['unassessed_resources']) == 49
results.append('A new case is incomplete and leaves every resource unassessed')
try:
    module.initialize(case_dir, 'Overwrite attempt')
    raise AssertionError('Existing case was overwritten')
except ValueError:
    assert json.loads((case_dir/'case.json').read_text()) == fresh
results.append('Initialization refuses to overwrite a resumable case')

original_library = module.library
def future_library(name):
    value = original_library(name)
    if name == 'core.json':
        value = copy.deepcopy(value)
        value['version'] = 'fictional-future-version'
        value['activities'].pop()
    return value
module.library = future_library
assert module.check(case_dir)['valid']
assert module.check(case_dir)['core_total'] == len(fresh['core'])
module.library = original_library
results.append('Resumption uses its frozen core contract even if the current skill baseline changes')

bad = copy.deepcopy(fresh)
bad['core'][0].update(state='credited', check='Claimed done', reviewer='fixture', date='2026-09-06')
save(bad)
assert not module.check(case_dir)['valid']
results.append('Claimed prior-work credit without inspected artifacts is rejected')

bad = copy.deepcopy(fresh)
bad['core'][0].update(state='considered', check='Skip setup', reviewer='fixture', date='2026-09-06')
save(bad)
assert not module.check(case_dir)['valid']
results.append('Mandatory work cannot be satisfied by an omission disposition')

bad = copy.deepcopy(fresh)
(case_dir/'artifacts/initial-handoff.md').write_text('Fictional initial plan; no customer study has run.', encoding='utf-8')
bad['artifacts'] = [{'id':'A-HANDOFF','path':'artifacts/initial-handoff.md','status':'checked'}]
handoff = next(row for row in bad['core'] if row['id']=='DS-NEXT-STEPS')
handoff.update(state='done', artifact_ids=['A-HANDOFF'], check='Initial action assigned', reviewer='fixture', date='2026-09-06')
save(bad)
result = module.check(case_dir)
assert not result['valid'] and 'DS-NEXT-STEPS' in result['pending_core']
assert not any('missing artifact' in error.lower() for error in result['errors'])
results.append('An initial action plan cannot complete the post-customer-study handoff')

bad = copy.deepcopy(fresh)
bad['resources'].pop()
save(bad)
assert not module.check(case_dir)['valid']
results.append('Dropping a catalog resource is rejected')

bad = copy.deepcopy(fresh)
bad['evidence'] = [{'id':'E1','kind':'synthetic','source':'fictional fixture','observation':'Invented test data',
                    'audience':'fictional','context':'checker test','date':'2026-09-06'}]
bad['hypotheses'] = [{'id':'H1','claim':'Fictional claim','evidence_ids':['missing']}]
save(bad)
assert not module.check(case_dir)['valid']
results.append('An evidence reference must resolve to an actual record')

stopped = copy.deepcopy(fresh)
stopped['lifecycle'] = 'stopped'
stopped['scope']['success_criteria'] = ['Fictional personal usefulness criterion']
stopped['scope']['next_investment'] = 'No further work on this fictional proposition'
for row in stopped['resources']:
    row.update(state='deferred', reason='Fictional case stopped before selecting any session')
stopped['decisions'] = [{'recommendation':'stop','evidence_ids':[],
                         'rationale':'User elected to stop the fictional case'}]
stopped['next_action'].update(action='None—case stopped', resume_trigger='User elects to reopen')
save(stopped)
before = (case_dir/'case.json').read_bytes()
checked = module.check(case_dir, decision=True)
assert checked['valid'] and checked['core_status'] == 'stopped—core incomplete'
assert (case_dir/'case.json').read_bytes() == before
results.append('Early stop permits a decision while preserving the incomplete checklist and history')

report = {'checks_passed':len(results),'results':results,'fixture_directory':str(fixture_root),
          'limit':'Structural checks do not establish artifact adequacy or real customer evidence.'}
(root/'.scratch/mentor-room/structural-checks.json').write_text(
    json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
