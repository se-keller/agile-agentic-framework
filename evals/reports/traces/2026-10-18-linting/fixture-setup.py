from pathlib import Path
import subprocess, shutil, json, hashlib
root=Path.cwd(); dest=Path('/private/tmp/aaf-lint-20261018'); dest.mkdir(exist_ok=True)
base=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip()
fw=dest/'agile-agentic-framework'; fw.mkdir(exist_ok=True)
archive=subprocess.Popen(['git','archive',base],stdout=subprocess.PIPE)
subprocess.run(['tar','-xf','-','-C',str(fw)],stdin=archive.stdout,check=True); archive.stdout.close(); archive.wait()
changed=subprocess.check_output(['git','diff','--name-only'],text=True).splitlines()
for f in changed:
 p=root/f
 if p.is_file():
  out=fw/f; out.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(p,out)
product=dest/'product'; shutil.copytree(fw/'skills/bootstrap-product-development/assets/product-development-skeleton',product,dirs_exist_ok=True)
for p in product.rglob('*'):
 if p.is_file():
  s=p.read_text()
  for a,b in {'{{PRODUCT_NAME}}':'Greeting','{{PRODUCT_SLUG}}':'greeting','{{GENERATED_DATE}}':'2026-10-18','{{GENERATED_AT}}':'2026-10-18T10:00:00Z','{{FRAMEWORK_REVISION}}':base}.items():s=s.replace(a,b)
  p.write_text(s)
code=product/'product-code'; code.mkdir(exist_ok=True)
(code/'greeting.py').write_text('def greet(name):\n    return f"Hello, {name}!"\n')
(code/'test_greeting.py').write_text('import unittest\n\nfrom greeting import greet\n\n\nclass GreetingTest(unittest.TestCase):\n    def test_named_user(self):\n        self.assertEqual(greet("Ada"), "Hello, Ada!")\n\n\nif __name__ == "__main__":\n    unittest.main()\n')
def artifact(path,typ,body,extra=''):
 p=product/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(f'---\ntype: {typ}\ncreated: "2026-10-18"\nupdated: "2026-10-18"\n{extra}---\n\n{body}\n')
sprint='artefacts/sprints/sprint-001/sprint-backlog/'
artifact(sprint+'sprint-goal.md','Sprint Goal','# Sprint Goal\n\nA user receives a personal greeting.')
artifact(sprint+'pbi-0001-greet.md','Product Backlog Item','# Greeting\n\nAs a user I want a greeting using my name.\n\nAC: Input Ada yields exactly Hello, Ada!.', 'id: pbi-0001\nbacklog_state: selected\n')
artifact(sprint+'developer-plan.md','Developer Plan','# Developer Plan\n\nImplement the greeting with Python. Automated named-user test, independent Tester check, PO assessment, collective Done. Sprint active; setup work is allowed. No UI.')
artifact('artefacts/product-backlog/product-vision.md','Product Vision','# Vision\n\nMake personal greetings easy.')
artifact('artefacts/product-backlog/current-product-goal.md','Product Goal','# Goal\n\nUsers receive a greeting with their name.')
(product/sprint/'index.md').write_text('# Active Sprint\n\n- [Goal](sprint-goal.md)\n- [Selected PBI](pbi-0001-greet.md)\n- [Plan](developer-plan.md)\n')
manifest={'target':base,'candidate_files':{f:hashlib.sha256((root/f).read_bytes()).hexdigest() for f in changed if (root/f).is_file()},'fixture':str(dest)}
(dest/'candidate.json').write_text(json.dumps(manifest,indent=2)+'\n')
for name in ['assessment','planning','handoff']:
 shutil.copytree(product,dest/name,dirs_exist_ok=True)
print(dest)
