"""Check configuration invariants; never claims to verify a live human approval."""
import json
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
ruleset = json.loads((root / '.github/rulesets/main.json').read_text())
assert ruleset['bypass_actors'] == [], 'No bypass actors permitted'
rules = {r['type']: r.get('parameters', {}) for r in ruleset['rules']}
review = rules['pull_request']
assert review['required_approving_review_count'] >= 1
assert all(review[key] for key in ('require_code_owner_review', 'require_last_push_approval', 'dismiss_stale_reviews_on_push', 'required_review_thread_resolution'))
assert rules['required_status_checks']['strict_required_status_checks_policy']
assert all(r in rules for r in ('deletion', 'non_fast_forward', 'required_signatures'))
owners = (root / '.github/CODEOWNERS').read_text()
assert re.search(r'^\*\s+@\S+', owners, re.M), 'All paths must have a human owner'
for path in (root / '.github/workflows').glob('*.y*ml'):
    text = path.read_text()
    assert not re.search(r'^\s*(pull_request_target|workflow_run|issue_comment)\s*:', text, re.M), path
    assert not re.search(r'permissions:\s*write-all', text), path
    for action in re.findall(r'uses:\s*([^\s]+)', text):
        assert re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_./-]+@[0-9a-f]{40}', action), (path, action)
print('PASS: proposed review configuration and action pins; live approval enforcement is not tested here')
