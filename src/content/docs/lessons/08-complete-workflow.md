---
title: 'Lesson 08 — A Complete Beginner Workflow'
sidebar:
  order: 8
---

## Goal

Practice the full Git/GitHub workflow from start to finish in a learner-owned practice repository.

## Full workflow

```text
clone → branch → edit → status → diff → add → commit → push → PR → review → merge → pull
```

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

## Checklist

### 1. Clone or open the repository

If you do not already have it locally:

```bash
git clone https://github.com/your-account/git-basics-sql-practice.git
cd git-basics-sql-practice
```

- [ ] I am inside the repository folder.

### 2. Start from main

```bash
git checkout main
git pull
```

or:

```bash
git switch main
git pull
```

- [ ] I am on an up-to-date `main` branch.

### 3. Create a branch

```bash
git checkout -b metadata/define-visit-date
```

or:

```bash
git switch -c metadata/define-visit-date
```

- [ ] I created a branch for my change.

### 4. Make a small change

Edit one data dictionary entry.

Keep the change small enough that a reviewer can understand it quickly.

- [ ] I made one small change.

### 5. Check status and diff

```bash
git status
git diff
```

- [ ] I can see my changed file.
- [ ] I reviewed the exact lines that changed.
- [ ] I do not see unrelated edits.

### 6. Stage the change

```bash
git add data-dictionary/patient_visits.md
```

- [ ] I staged the file.

### 7. Commit the change

```bash
git commit -m "docs: define visit date field"
```

- [ ] I committed the change.

### 8. Push the branch

```bash
git push -u origin metadata/define-visit-date
```

- [ ] I pushed the branch to GitHub.

### 9. Open a pull request

- [ ] I opened GitHub.
- [ ] I created a PR from my branch into `main`.
- [ ] I added a short title and description.

### 10. Update if needed

If feedback is requested:

```bash
git status
git diff
git add data-dictionary/patient_visits.md
git commit -m "docs: address feedback"
git push
```

- [ ] I understand that pushing to the same branch updates the PR.

### 11. Merge the PR

After review:

- [ ] The PR is approved or ready.
- [ ] The PR is merged.
- [ ] The branch is deleted on GitHub if no longer needed.

### 12. Update local main

```bash
git checkout main
git pull
```

or:

```bash
git switch main
git pull
```

- [ ] My local `main` has the merged change.

## Final completion check

- [ ] I completed one full Git/GitHub workflow.
- [ ] I can describe each step in my own words.
- [ ] I know to use branches instead of changing `main` directly.
- [ ] I know to use PRs for review before merging.
- [ ] I know to run `git status` often.
- [ ] I know to run `git diff` before staging.
