# Lesson 08 — A Complete Beginner Workflow

## Goal

Practice the full Git/GitHub workflow from start to finish in a learner-owned practice repository.

By this point, the commands should start to feel less like separate facts and more like one repeatable work pattern.

## Full workflow

```text
start updated → branch → edit → inspect → stage → commit → push → PR → review → merge → update main
```

More explicitly:

```text
clone/open → switch main → pull → branch → edit → status → diff → add → diff --staged
          → commit → push → open PR → respond to review → merge → switch main → pull
```

## What each step is protecting

| Step | What it protects |
| --- | --- |
| `git pull` before starting | You do not build on stale work. |
| Branching | `main` stays stable while you work. |
| `git status` | You know what Git sees. |
| `git diff` | You catch accidental edits before staging. |
| Staging specific files | The commit contains only the intended change. |
| Committing | Your work has a local checkpoint. |
| Pushing | GitHub has your branch and commits. |
| Pull request | Someone can review before the change enters `main`. |
| Pulling after merge | Your computer catches up with GitHub. |

> **Adult-learning note:** The goal is not to do this from memory immediately. Use the checklist until the rhythm becomes ordinary.

## Practice scenario

Use `git-basics-sql-practice` or another `git-basics-` template repository.

Scenario: improve one data dictionary entry so another analyst can understand a field without asking for clarification.

Example file:

```text
data-dictionary/patient_visits.md
```

Example branch:

```text
metadata/define-visit-date
```

Example commit message:

```text
docs: define visit date field
```

## Checklist

### 1. Clone or open the repository

If you do not already have it locally:

```bash
git clone https://github.com/your-account/git-basics-sql-practice.git
cd git-basics-sql-practice
```

If you already cloned it, open your terminal in that repository folder.

Check:

```bash
git status
```

- [ ] I am inside the repository folder.
- [ ] `git status` works without an error.

### 2. Start from main

```bash
git switch main
git pull
```

If your Git version does not support `switch`, use:

```bash
git checkout main
git pull
```

- [ ] I am on an up-to-date `main` branch.

### 3. Create a branch

```bash
git switch -c metadata/define-visit-date
```

Or:

```bash
git checkout -b metadata/define-visit-date
```

Confirm:

```bash
git status
```

- [ ] I created a branch for my change.
- [ ] `git status` shows I am on that branch.

### 4. Make a small change

Edit one data dictionary entry in:

```text
data-dictionary/patient_visits.md
```

Keep the change small enough that a reviewer can understand it quickly.

Example revision:

```markdown
- `visit_date`: Calendar date when the visit occurred, recorded in YYYY-MM-DD format.
```

- [ ] I made one small change.
- [ ] I saved the file.

### 5. Check status and diff

```bash
git status
git diff
```

Before continuing, answer:

| Question | Answer |
| --- | --- |
| Which branch am I on? |  |
| Which file changed? |  |
| Are the changed lines intentional? |  |

- [ ] I can see my changed file.
- [ ] I reviewed the exact lines that changed.
- [ ] I do not see unrelated edits.

### 6. Stage the change

```bash
git add data-dictionary/patient_visits.md
```

Check the staged version:

```bash
git diff --staged
```

- [ ] I staged the file.
- [ ] I checked what is staged.

### 7. Commit the change

```bash
git commit -m "docs: define visit date field"
```

Then run:

```bash
git status
```

- [ ] I committed the change.
- [ ] I know whether my branch is ahead of GitHub.

### 8. Push the branch

```bash
git push -u origin metadata/define-visit-date
```

Expected result: Git sends the branch and commit to GitHub. The terminal may also print a link for opening a pull request.

- [ ] I pushed the branch to GitHub.

### 9. Open a pull request

On GitHub:

- choose your branch as the source branch,
- choose `main` as the target branch,
- write a short title,
- explain what changed and why.

Useful PR description:

```text
Defines the visit_date field so analysts know the expected date format.

Checks:
- Reviewed git diff locally
- Updated one data dictionary entry only
```

- [ ] I opened GitHub.
- [ ] I created a PR from my branch into `main`.
- [ ] I added a short title and description.

### 10. Update if needed

If feedback is requested, stay on the same branch and make another commit:

```bash
git status
git diff
git add data-dictionary/patient_visits.md
git diff --staged
git commit -m "docs: address feedback"
git push
```

Pushing to the same branch updates the existing PR.

- [ ] I understand that pushing to the same branch updates the PR.

### 11. Merge the PR

After review:

- [ ] The PR is approved or ready.
- [ ] The PR is merged.
- [ ] The branch is deleted on GitHub if no longer needed.

### 12. Update local main

```bash
git switch main
git pull
```

Or:

```bash
git checkout main
git pull
```

- [ ] My local `main` has the merged change.

## The full workflow as a decision table

| If this is true... | Do this next |
| --- | --- |
| You are not in the repository folder | `cd` into the repository, then run `git status` |
| You are on `main` and about to edit | Create a branch first |
| You edited a file | Run `git status` and `git diff` |
| The diff shows unrelated changes | Stop and clean up before staging |
| The diff shows the intended change | `git add filename` |
| Work is staged | `git diff --staged`, then commit |
| Your branch is ahead locally | `git push` |
| The PR was merged | Switch to `main` and pull |

## Final completion check

- [ ] I completed one full Git/GitHub workflow.
- [ ] I can describe what Git knows, what GitHub has, what changed, and what happens next.
- [ ] I know to use branches instead of changing `main` directly.
- [ ] I know to use PRs for review before merging.
- [ ] I know that `git push` sends commits and does not commit file changes.
- [ ] I know to run `git status` often.
- [ ] I know to run `git diff` before staging.
