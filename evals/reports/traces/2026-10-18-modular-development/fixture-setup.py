from pathlib import Path
import subprocess,shutil,json,hashlib
root=Path.cwd(); base=Path('/private/tmp/aaf-solid-20261018');base.mkdir()
commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
fw=base/'agile-agentic-framework';fw.mkdir()
a=subprocess.Popen(['git','archive',commit],stdout=subprocess.PIPE)
subprocess.run(['tar','-xf','-','-C',str(fw)],stdin=a.stdout,check=True);a.stdout.close();assert a.wait()==0
skeleton=fw/'skills/bootstrap-product-development/assets/product-development-skeleton'
def artifact(p,typ,body,extra=''):
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(f'---\ntype: {typ}\ncreated: "2026-10-18"\nupdated: "2026-10-18"\n{extra}---\n\n{body}\n')
def product(name):
 p=base/name;shutil.copytree(skeleton,p)
 for f in p.rglob('*'):
  if f.is_file():
   t=f.read_text()
   for k,v in {'PRODUCT_NAME':name,'PRODUCT_SLUG':name,'GENERATED_DATE':'2026-10-18','GENERATED_AT':'2026-10-18T10:00:00Z','FRAMEWORK_REVISION':commit,'FRAMEWORK_REPOSITORY':'https://github.com/se-keller/agile-agentic-framework','FRAMEWORK_DIRECTORY':'agile-agentic-framework'}.items():t=t.replace('{{'+k+'}}',v)
   f.write_text(t)
 code=p/'product-code';code.mkdir(exist_ok=True)
 (p/'evidence').mkdir()
 (code/'.flake8').write_text('[flake8]\nmax-line-length = 79\n')
 (code/'requirements-dev.txt').write_text('flake8==7.3.0\npycodestyle==2.14.0\npyflakes==3.4.0\nmccabe==0.7.0\n')
 (code/'check.py').write_text('''from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent
for args in [("-m", "flake8", "."),
             ("-m", "unittest", "discover", "-s", ".", "-v")]:
    result = subprocess.run([sys.executable, *args], cwd=ROOT, check=False)
    if result.returncode:
        sys.exit(result.returncode)
''')
 artifact(p/'artefacts/product-backlog/product-vision.md','Product Vision','# Vision\n\nReliable customer checkout and usable receipts.')
 artifact(p/'artefacts/product-backlog/current-product-goal.md','Product Goal','# Product Goal\n\nCustomers see correct discounted totals with usable audit receipts.')
 return p
checkout=product('checkout')
code=checkout/'product-code'
(code/'checkout.py').write_text('''from pathlib import Path

from gateway import charge


def checkout(order, audit_path="audit.log"):
    if not order["items"]:
        raise ValueError("empty order")
    total = sum(item["price"] * item["quantity"] for item in order["items"])
    record = f"order:{order['id']} total:{total}"
    Path(audit_path).write_text(record, encoding="utf-8")
    payment = charge(order, total)
    return {"total": total, "payment": payment}
''')
(code/'gateway.py').write_text('''def charge(order, total):
    if order.get("decline"):
        raise ValueError("payment declined")
    return "paid"
''')
(code/'test_checkout.py').write_text('''from pathlib import Path
import tempfile
import unittest

from checkout import checkout


class CheckoutTest(unittest.TestCase):
    def test_original_result(self):
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "audit.log")
            order = {"id": "a", "items": [{"price": 100, "quantity": 1}]}
            self.assertEqual(checkout(order, path),
                             {"total": 100, "payment": "paid"})

    def test_empty_error(self):
        with self.assertRaisesRegex(ValueError, "^empty order$"):
            checkout({"id": "a", "items": []})

    def test_payment_error(self):
        with tempfile.TemporaryDirectory() as directory:
            order = {"id": "a", "items": [{"price": 100, "quantity": 1}],
                     "decline": True}
            with self.assertRaisesRegex(ValueError, "^payment declined$"):
                checkout(order, str(Path(directory) / "audit.log"))
''')
sprint='artefacts/sprints/sprint-001/sprint-backlog'
def selected(p,goal,pbi,plan):
 d=p/sprint
 artifact(d/'sprint-goal.md','Sprint Goal','# Sprint Goal\n\n'+goal)
 artifact(d/'pbi-0001.md','Product Backlog Item','# Selected PBI\n\n'+pbi,'id: pbi-0001\nbacklog_state: selected\n')
 artifact(d/'developer-plan.md','Developer Plan','# Developer Plan\n\n'+plan)
 (d/'index.md').write_text('# Active Sprint\n\n- [Goal](sprint-goal.md)\n- [Selected PBI](pbi-0001.md)\n- [Plan](developer-plan.md)\n')
 (p/'artefacts/sprints/index.md').write_text('# Sprints\n\n- [Active sprint](sprint-001/sprint-backlog/index.md)\n')
selected(checkout,'Customer totals reflect SAVE10 and Operations receives JSON receipts.', 'Finance requests SAVE10: total 100 -> 90; without promotion total unchanged. Operations requests JSON audit with order_id and total. Public checkout(order, audit_path="audit.log") result keys and ValueError messages stay stable; audit persists before payment, including failed payment. No UI or actual network exists in this fixture.', 'Active Sprint; implement one PBI. Preserve public behavior, add discounted result and JSON receipt, focused tests, current lint, independent source review before handoff, then independent acceptance. Python; no existing CI. No other PBI work starts.')
# Planning fixtures share product direction and code, but have no active Sprint.
planning=base/'planning';shutil.copytree(checkout,planning)
shutil.rmtree(planning/'artefacts/sprints/sprint-001')
(planning/'artefacts/sprints/index.md').write_text('# Sprints\n\nNo active Sprint.\n')
artifact(planning/'artefacts/product-backlog/items/pbi-0001.md','Product Backlog Item','# Proposed checkout change\n\nFinance SAVE10 total 100 -> 90; Operations wants JSON receipt. Existing result/error contracts stable.','id: pbi-0001\nbacklog_state: ready\n')
artifact(planning/'artefacts/developer-plan.md','Developer Plan','# Pending Developer Plan\n\nTester cases: SAVE10 100 -> 90, no promo unchanged; JSON receipt order_id/total, existing empty-order and payment error contracts preserved. No selection or final Goal yet.')
small=product('cohesive'); c=small/'product-code'
entries=['    "welcome": "Welcom",']+[f'    "item_{i}": "Item {i}",' for i in range(340)]
(c/'labels.py').write_text('LABELS = {\n'+'\n'.join(entries)+'\n}\n\n\ndef label_for(key):\n    return LABELS[key]\n')
(c/'test_labels.py').write_text('''import unittest

from labels import label_for


class LabelTest(unittest.TestCase):
    def test_existing_entry(self):
        self.assertEqual(label_for("item_0"), "Item 0")
''')
(c/'structure-signals.json').write_text(json.dumps({'review_signal_lines':300,'meaning':'Inspect cohesive responsibilities; not a split mandate.'},indent=2)+'\n')
selected(small,'Users see the correctly spelled welcome label.','Change label_for("welcome") from Welcom to Welcome. Other lookups and unknown-key KeyError remain unchanged.','Active Sprint; one cohesive table and lookup function, no infrastructure. Product size signal exceeded; inspect before choosing refactoring. Independent reviewer available through host.')
fix=product('fix'); c=fix/'product-code'
(c/'greeting.py').write_text('def greet(name):\n    return "Hello!"\n')
(c/'test_greeting.py').write_text('''import unittest

from greeting import greet


class GreetingTest(unittest.TestCase):
    def test_named(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")
''')
selected(fix,'Personal greeting works.','Input Ada yields exactly Hello, Ada!.','Active Sprint. Open Bug is highest priority; preserve Tester failure, fix source, regression tests, independent structure review then fix-ready and Tester retest. No Done or release.')
b=fix/sprint
artifact(b/'bug-0001.md','Bug','# Missing name\n\nInput Ada expected Hello, Ada!, actual Hello!. Failed required test is in workspace evidence/failed-test.json. Highest priority; independent retest pending.','id: bug-0001\nbug_state: open\n')
(b/'index.md').write_text((b/'index.md').read_text().replace('# Active Sprint','# Active Sprint\n\n- [Open Bug, top priority](bug-0001.md)'))
r=subprocess.run(['/Users/sebastiankeller/miniconda3/bin/python','-m','unittest','discover','-s','product-code','-v'],cwd=fix,capture_output=True,text=True)
(fix/'evidence/failed-test.json').write_text(json.dumps({'command':'python -m unittest discover -s product-code -v','exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr},indent=2)+'\n')
assessment=base/'assessment';shutil.copytree(checkout,assessment)
# Every product starts from a real baseline, so exact source diffs are inspectable.
for p in [checkout,planning,small,fix,assessment]:
 for cmd in [['git','init','-q'],['git','add','.'],['git','-c','user.name=Evaluation Harness','-c','user.email=eval@example.invalid','commit','-qm','Seed disposable product fixture']]:subprocess.run(cmd,cwd=p,check=True)
changed=subprocess.check_output(['git','diff','--name-only'],text=True).splitlines()
for f in changed:
 p=root/f
 if p.is_file():
  dest=fw/f;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
(base/'candidate.json').write_text(json.dumps({'target':commit,'files':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in changed if (root/f).is_file()}},indent=2)+'\n')
print(base)
