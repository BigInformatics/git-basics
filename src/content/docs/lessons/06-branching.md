---
title: 'Lesson 06 — Branching'
sidebar:
  order: 6
---

## Goal

Create a branch so you can work safely without changing `main` directly.

## What a branch is

A **branch** is a separate workspace for a change.

Instead of editing `main` directly, create a branch for your work.

![Diagram showing main as the stable shared line and a branch splitting off as a safe workspace for one proposed change.](/git-basics/images/git-branch-workspace.svg)

```text
main        = official shared version
your branch = your workspace for a proposed change
```

## Local and GitHub view

![Diagram showing main on your computer and origin/main on GitHub, plus a new local branch that appears on GitHub only after you push it.](/git-basics/images/git-local-github-branch-view.svg)

A branch starts on your computer. It appears on GitHub after you push it.

## Checklist

### 1. Start from main

Run:

```bash
git checkout main
```

or:

```bash
git switch main
```

- [ ] I am on `main`.

### 2. Pull the latest main

Run:

```bash
git pull
```

- [ ] My local `main` is up to date.

### 3. Create a new branch

For a SQL query documentation change, run:

```bash
git checkout -b analysis/clarify-visit-query
```

or:

```bash
git switch -c analysis/clarify-visit-query
```

- [ ] I created and switched to a new branch.

### 4. Confirm the current branch

Run:

```bash
git branch
```

The current branch has an asterisk next to it.

- [ ] I can identify my current branch.

### 5. Make and commit a change

Use the workflow from Lesson 04:

```bash
git status
git diff
git add queries/01-count-visits.sql
git commit -m "docs: clarify visit count query"
```

- [ ] I committed a change on my branch.

### 6. Push the branch to GitHub

Run:

```bash
git push -u origin analysis/clarify-visit-query
```

- [ ] My branch exists on GitHub.

## Branch naming examples

```text
docs/add-analysis-note
analysis/clarify-visit-query
metadata/define-visit-date
fix/correct-county-label
```

Use names that describe the change. Avoid branch names like `updates`, `work`, or `stuff`.

## Completion check

- [ ] I can create a branch.
- [ ] I can switch branches.
- [ ] I can commit on a branch.
- [ ] I can push a branch to GitHub.
- [ ] I understand that a branch is safer than editing `main` directly.
