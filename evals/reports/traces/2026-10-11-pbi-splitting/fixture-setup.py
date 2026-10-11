from pathlib import Path
import subprocess, shutil, hashlib, json, datetime

repo = Path('/Users/sebastiankeller/Documents/devenv/agile-agentic-framework')
root = Path('/private/tmp/aaf-pbi-splitting-20261011')
target = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=repo, text=True).strip()
framework = root / 'agile-agentic-framework'
if not framework.exists():
    subprocess.run(['git', 'clone', '--local', '--no-hardlinks', str(repo), str(framework)], check=True, capture_output=True)
    subprocess.run(['git', 'checkout', '--detach', target], cwd=framework, check=True, capture_output=True)
for label in ['Split 001', 'Split 002', 'Boundary PO', 'Planning Critical']:
    if not (root / ('product-development-' + label.lower().replace(' ', '-'))).exists():
        subprocess.run(['python', str(framework / 'skills/bootstrap-product-development/scripts/bootstrap.py'), label, '--parent', str(root)], check=True)
paths = [
    'skills/product-backlog-item-splitting/SKILL.md',
    'skills/agent-core-skills/product-owner-core/references/manage-product-backlog.md',
    'skills/agent-core-skills/developer-core/references/participate-in-sprint-planning.md',
    'skills/bootstrap-product-development/assets/product-development-skeleton/artefacts/definition-of-ready.md',
]
for rel in paths:
    dest = framework / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(repo / rel, dest)
(root / 'candidate.json').write_text(json.dumps({'target': target, 'files': {p: hashlib.sha256((repo / p).read_bytes()).hexdigest() for p in paths}}, indent=2) + '\n')
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
date = now[:10]
def concept(path, kind, title, body, extra=''):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f'---\ntype: {kind}\ntitle: {title}\nstatus: stable\ncreated: "{date}"\nupdated: "{date}"\ngenerated: {{ by: "process:evaluation-fixture", at: "{now}" }}\n{extra}---\n\n# {title}\n\n{body}\n')
for name in ['split-001', 'split-002', 'boundary-po', 'planning-critical']:
    workspace = root / ('product-development-' + name)
    artefacts = workspace / 'artefacts'
    (workspace / 'evidence').mkdir(exist_ok=True)
    ready = (framework / paths[-1]).read_text().replace('{{GENERATED_DATE}}', date).replace('{{GENERATED_AT}}', now).replace('{{PRODUCT_SLUG}}', name)
    (artefacts / 'definition-of-ready.md').write_text(ready)
    if name in ['split-001', 'boundary-po']:
        vision = 'Kundinnen verwalten ihre bestehenden Konten selbstbestimmt. Registrierung besteht bereits. Der Dienst soll aktuelle Kontaktdaten und einen selbstbestimmten Ausstieg ermöglichen.'
        goal = 'Bestehende Kundinnen können Kontaktname und E-Mail-Adresse aktualisieren sowie ihr Konto kündigen. Nach Kündigung ist der Dienstzugang beendet; ein erneuter Zugang mit dem gekündigten Konto ist nicht möglich. Physische Datenlöschung und laufende Zahlungsverträge gehören nicht zum aktuellen Ziel. Das Team kann mehrere vergleichbare PBIs pro Sprint liefern.'
    else:
        vision = 'Kunden veröffentlichen Anfragen, damit andere auf ihre Bedürfnisse reagieren können. Managerfreigaben unterstützen Anfragen, für die ein Review gewünscht ist.'
        goal = 'Kunden können eine vollständige Anfrage einreichen und veröffentlichen. Normale Anfragen dürfen unmittelbar veröffentlicht werden. Bei ausdrücklich managergeprüften Anfragen muss eine Freigabe vor Veröffentlichung erfolgen; eine abgelehnte Anfrage bleibt unveröffentlicht. Das Team kann mehrere vergleichbare PBIs pro Sprint liefern.'
    verified = f'verified: {{ by: "human:fixture-maintainer", at: "{now}" }}\n'
    concept(artefacts / 'product-backlog/product-vision.md', 'Product Vision', 'Product Vision', vision, verified)
    concept(artefacts / 'product-backlog/current-product-goal.md', 'Product Goal', 'Current Product Goal', goal, verified)
    if name != 'split-001':
        items = [('pbi-0001', 'request-publication', 'Als Kunde möchte ich eine Anfrage einreichen, durch einen Manager freigeben lassen und veröffentlichen, damit andere auf meinen Bedarf reagieren können.', ['AC1: Eine vollständige eingereichte Anfrage kann durch den Manager freigegeben werden.', 'AC2: Nach Freigabe ist die Anfrage veröffentlicht und für andere sichtbar.', 'AC3: Eine abgelehnte Anfrage bleibt unveröffentlicht.'])]
        if name == 'boundary-po':
            items = [('pbi-0001', 'contact-details', 'Als Kundin möchte ich meine Kontaktdaten aktualisieren, damit der Dienst mich zuverlässig erreicht.', ['AC1: Geänderte Kontaktname und E-Mail-Adresse sind bei erneutem Anzeigen sichtbar.'])]
        if name == 'planning-critical':
            items += [('pbi-0002', 'read-own-request', 'Als Kunde möchte ich meine eingereichte Anfrage ansehen, damit ich ihren Inhalt prüfen kann.', ['AC1: Die Kundin sieht den Inhalt ihrer eigenen eingereichten Anfrage.']), ('pbi-0003', 'withdraw-request', 'Als Kunde möchte ich eine eigene Anfrage zurückziehen, damit sie keine weiteren Antworten erhält.', ['AC1: Eine zurückgezogene Anfrage erscheint nicht mehr im Angebot für andere.'])]
        links = []
        for id_, slug, summary, criteria in items:
            filename = f'{id_}-{slug}.md'
            concept(artefacts / 'product-backlog/items' / filename, 'Product Backlog Item', slug, summary + '\n\n## Acceptance Criteria\n\n' + '\n'.join('- ' + c for c in criteria) + '\n\n## Open questions\n\nNone material for presenting the existing scope.', f'id: {id_}\nbacklog_state: ready\n')
            links.append(f'- [{id_}: {slug}](items/{filename})')
        index = artefacts / 'product-backlog/index.md'
        text = index.read_text()
        text = text[:text.index('No Product Backlog Items')] + '\n'.join(links) + '\n'
        index.write_text(text)
    code = workspace / 'product-code' / 'existing-product.txt'
    code.parent.mkdir(parents=True, exist_ok=True)
    code.write_text('Existing product context. Registration is already available. Evaluation fixture: Product Code execution is unnecessary during Planning.\n')
    subprocess.run(['python', str(framework / 'skills/okf/scripts/validate_okf.py'), str(artefacts)], check=True)
    subprocess.run(['git', 'add', '.'], cwd=workspace, check=True)
    subprocess.run(['git', '-c', 'user.name=Evaluation Fixture', '-c', 'user.email=eval@example.invalid', 'commit', '-m', 'Prepare baseline evaluation fixture'], cwd=workspace, check=True, capture_output=True)
print(root)
