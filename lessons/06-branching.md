# Lesson 06 — Branching

## Goal

Create a branch so you can work safely without changing `main` directly.

## What a branch is

A **branch** is a separate workspace for a change.

Instead of editing `main` directly, create a branch for your work.

```text
main = official shared version
your branch = your workspace for a proposed change
```

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

Run:

```bash
git checkout -b docs/practice-change
```

or:

```bash
git switch -c docs/practice-change
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
git add filename
git commit -m "docs: make practice branch change"
```

- [ ] I committed a change on my branch.

### 6. Push the branch to GitHub

Run:

```bash
git push -u origin docs/practice-change
```

- [ ] My branch exists on GitHub.

## Branch naming examples

```text
docs/update-readme
analysis/add-summary-table
fix/correct-date-label
feature/add-data-dictionary
```

## Completion check

- [ ] I can create a branch.
- [ ] I can switch branches.
- [ ] I can commit on a branch.
- [ ] I can push a branch to GitHub.
