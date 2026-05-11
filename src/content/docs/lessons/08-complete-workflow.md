---
title: 'Lesson 08 — A Complete Beginner Workflow'
sidebar:
  order: 8
---

## Goal

Practice the full Git/GitHub workflow from start to finish.

## Full workflow

```text
clone → branch → edit → status → add → commit → push → PR → review → merge → pull
```

## Checklist

### 1. Clone or open the repository

If you do not already have it locally:

```bash
git clone https://github.com/organization/repository-name.git
cd repository-name
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
git checkout -b docs/add-practice-note
```

or:

```bash
git switch -c docs/add-practice-note
```

- [ ] I created a branch for my change.

### 4. Make a small change

Edit a file, such as `README.md`.

- [ ] I made one small change.

### 5. Check status

```bash
git status
```

- [ ] I can see my changed file.

### 6. Stage the change

```bash
git add README.md
```

- [ ] I staged the file.

### 7. Commit the change

```bash
git commit -m "docs: add practice note"
```

- [ ] I committed the change.

### 8. Push the branch

```bash
git push -u origin docs/add-practice-note
```

- [ ] I pushed the branch to GitHub.

### 9. Open a pull request

- [ ] I opened GitHub.
- [ ] I created a PR from my branch into `main`.
- [ ] I added a short title and description.

### 10. Update if needed

If feedback is requested:

```bash
git add README.md
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
