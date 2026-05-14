from pathlib import Path
import subprocess
import shutil

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'tmp' / 'lesson-concept-sources'
IMG = ROOT / 'public' / 'images'
OUT.mkdir(parents=True, exist_ok=True)
IMG.mkdir(parents=True, exist_ok=True)

lessons = [
    {
        'num':'01','slug':'what-git-and-github-are','title':'What Git and GitHub do','subtitle':'Git saves project history. GitHub shares it for review and collaboration.',
        'left':'Your computer','right':'GitHub','steps':[('Project files','Scripts, notes, queries'),('Git history','Local commits'),('Shared remote','Team copy on GitHub')],
        'commands':['git status','git commit','git push'],
        'takeaway':'Git tracks work on your computer; GitHub makes committed work visible to the team.',
        'accent':'#2563eb'
    },
    {
        'num':'02','slug':'setup-and-orientation','title':'Setup and first orientation','subtitle':'Before changing files, confirm Git knows who you are and where you are.',
        'left':'Terminal checks','right':'Ready state','steps':[('git --version','Git is installed'),('git config user.name','Your commits have a name'),('git status','Repository folder confirmed')],
        'commands':['git --version','git config --global user.name','git status'],
        'takeaway':'Setup is not busywork: it prevents confusing commits and wrong-folder mistakes.',
        'accent':'#0f766e'
    },
    {
        'num':'03','slug':'cloning-a-repository','title':'Cloning a repository','subtitle':'Clone copies a GitHub repository into a local folder you can work in.',
        'left':'GitHub repo','right':'Local folder','steps':[('Files','Downloaded to your computer'),('History','Commits come with the clone'),('origin','Connection back to GitHub')],
        'commands':['git clone <url>','cd <repo>','git status'],
        'takeaway':'After cloning, you have both the files and the Git history, connected to origin.',
        'accent':'#7c3aed'
    },
    {
        'num':'04','slug':'status-staging-commits','title':'Status, staging, and commits','subtitle':'Move deliberately: inspect changes, stage the right file, then create a local checkpoint.',
        'left':'Working files','right':'Local history','steps':[('Edit','Change a file'),('Stage','Choose what goes next'),('Commit','Save a local checkpoint')],
        'commands':['git status','git diff','git add','git commit'],
        'takeaway':'A commit is local history. Review before staging, and review staged work before committing.',
        'accent':'#d97706'
    },
    {
        'num':'05','slug':'pushing-and-pulling','title':'Pushing and pulling','subtitle':'Push sends commits to GitHub. Pull brings shared commits back to your computer.',
        'left':'Local commits','right':'GitHub commits','steps':[('Commit first','Push needs committed work'),('Push →','Share your commits'),('← Pull','Receive shared updates')],
        'commands':['git pull','git commit','git push'],
        'takeaway':'If you only edited a file and did not commit, there is nothing for git push to send.',
        'accent':'#dc2626'
    },
    {
        'num':'06','slug':'branching','title':'Branching','subtitle':'A branch is a safe workspace for one proposed change.',
        'left':'main','right':'feature branch','steps':[('Start updated','Pull main first'),('Create branch','Work away from main'),('Push branch','Publish for PR')],
        'commands':['git pull','git switch -c analysis/change','git push -u origin HEAD'],
        'takeaway':'Local work becomes shared work when the branch is pushed.',
        'accent':'#16a34a'
    },
    {
        'num':'07','slug':'pull-requests','title':'Pull requests','subtitle':'A PR is the review bridge between your branch and shared main.',
        'left':'Your branch','right':'main','steps':[('Open PR','Describe the change'),('Review + CI','Check before merge'),('Merge','Accepted work joins main')],
        'commands':['git push -u origin HEAD','Open pull request','Review, update, merge'],
        'takeaway':'A pull request is not just paperwork; it is where the team confirms the change is safe.',
        'accent':'#0891b2'
    },
    {
        'num':'08','slug':'complete-workflow','title':'Complete beginner workflow','subtitle':'The full loop is repeatable: sync, branch, change, review, merge, sync again.',
        'left':'Start local','right':'Shared main','steps':[('Sync','Pull latest main'),('Work small','Branch, edit, commit'),('Collaborate','Push, PR, review, merge')],
        'commands':['git pull','git switch -c ...','git add && git commit','git push','Open PR'],
        'takeaway':'Small branches and small commits make the whole collaboration loop easier to review.',
        'accent':'#4f46e5'
    },
]

def html_for(l):
    step_cards = ''.join(f'<div class="step"><b>{a}</b><p>{b}</p></div>' for a,b in l['steps'])
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Lesson {l['num']} concept</title>
<style>
  * {{ box-sizing: border-box; }}
  body {{ margin:0; width:1600px; height:1000px; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; color:#172033; background:#f6f0e8; }}
  .frame {{ width:1600px; height:1000px; padding:58px; background:
      radial-gradient(circle at 10% 12%, rgba(255,255,255,.9), rgba(255,255,255,0) 28%),
      linear-gradient(135deg, #fbf7ef 0%, #efe3d3 100%); }}
  .card {{ height:884px; border-radius:42px; background:#fffaf3; border:2px solid rgba(23,32,51,.1); box-shadow:0 32px 80px rgba(74,52,34,.18); padding:48px; position:relative; overflow:hidden; }}
  .card:before {{ content:""; position:absolute; inset:0 0 auto 0; height:14px; background:{l['accent']}; opacity:.9; }}
  header {{ display:flex; align-items:start; justify-content:space-between; gap:28px; margin-bottom:34px; }}
  .eyebrow {{ color:{l['accent']}; font-weight:850; letter-spacing:.14em; text-transform:uppercase; font-size:24px; margin-bottom:12px; }}
  h1 {{ margin:0; font-size:68px; line-height:1.03; letter-spacing:-.05em; color:#111827; }}
  .subtitle {{ margin:20px 0 0; max-width:920px; font-size:30px; line-height:1.32; color:#4b5563; }}
  .badge {{ min-width:190px; text-align:center; border-radius:28px; padding:20px 24px; background:#fff; border:2px solid rgba(23,32,51,.12); color:#374151; font-size:24px; font-weight:800; box-shadow:0 10px 28px rgba(17,24,39,.08); }}
  .model {{ display:grid; grid-template-columns: 1fr 220px 1fr; align-items:center; gap:30px; margin:30px 0 32px; }}
  .zone {{ min-height:260px; background:#fff; border:2px solid rgba(17,24,39,.12); border-radius:34px; padding:28px; box-shadow:0 12px 34px rgba(17,24,39,.08); }}
  .zone h2 {{ margin:0 0 18px; font-size:34px; letter-spacing:-.03em; }}
  .pill {{ display:inline-flex; align-items:center; gap:10px; padding:13px 16px; border-radius:999px; background:color-mix(in srgb, {l['accent']} 12%, white); color:#111827; border:1px solid color-mix(in srgb, {l['accent']} 30%, white); font-weight:800; font-size:23px; margin:0 10px 12px 0; }}
  .arrow {{ text-align:center; color:#374151; font-weight:900; }}
  .arrow .line {{ height:8px; border-radius:99px; background:{l['accent']}; position:relative; margin:0 auto 18px; width:180px; }}
  .arrow .line:after {{ content:""; position:absolute; right:-2px; top:-10px; border-left:24px solid {l['accent']}; border-top:14px solid transparent; border-bottom:14px solid transparent; }}
  .arrow small {{ display:block; font-size:20px; line-height:1.2; color:#6b7280; }}
  .steps {{ display:grid; grid-template-columns: repeat(3, 1fr); gap:22px; margin-top:26px; }}
  .step {{ border-radius:22px; background:#f9fafb; border:1px solid rgba(17,24,39,.1); padding:20px 22px; min-height:120px; }}
  .step b {{ display:block; font-size:30px; margin-bottom:8px; color:#111827; }}
  .step p {{ margin:0; font-size:25px; line-height:1.28; color:#374151; }}
  .takeaway {{ position:absolute; left:48px; right:48px; bottom:42px; display:flex; gap:20px; align-items:center; border-radius:28px; background:#172033; color:#fff; padding:24px 28px; font-size:29px; line-height:1.25; }}
  .takeaway b {{ color:#fbbf24; white-space:nowrap; }}
</style>
</head>
<body>
  <main class="frame">
    <section class="card">
      <header>
        <div>
          <div class="eyebrow">Git Basics · Lesson {l['num']}</div>
          <h1>{l['title']}</h1>
          <p class="subtitle">{l['subtitle']}</p>
        </div>
        <div class="badge">Lesson map</div>
      </header>
      <section class="model" aria-label="lesson concept model">
        <div class="zone"><h2>{l['left']}</h2>{step_cards}</div>
        <div class="arrow"><div class="line"></div><small>work moves this way</small></div>
        <div class="zone"><h2>{l['right']}</h2><div class="pill">What Git knows</div><div class="pill">What GitHub has</div><div class="pill">What happens next</div></div>
      </section>
      <div class="takeaway"><b>Remember:</b><span>{l['takeaway']}</span></div>
    </section>
  </main>
</body>
</html>'''

chrome = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
if not Path(chrome).exists():
    chrome = shutil.which('google-chrome') or shutil.which('chromium') or shutil.which('chromium-browser')
if not chrome:
    raise SystemExit('Chrome/Chromium not found')

for l in lessons:
    name = f"git-lesson{l['num']}-concept-{l['slug']}"
    html = OUT / f'{name}.html'
    png = OUT / f'{name}.png'
    html.write_text(html_for(l))
    subprocess.run([chrome, '--headless', '--disable-gpu', '--hide-scrollbars', '--window-size=1600,1000', f'--screenshot={png}', f'file://{html}'], check=True)
    target = IMG / png.name
    target.write_bytes(png.read_bytes())
    print(target)
