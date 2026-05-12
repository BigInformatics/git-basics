---
title: 'Lesson 05 — Pushing and Pulling'
sidebar:
  order: 5
---

## Goal

Send commits to GitHub and bring updates from GitHub back to your computer.

## What push and pull mean

```bash
git push
```

Sends your local commits to GitHub.

```bash
git pull
```

Brings new commits from GitHub to your computer.

Important: `git push` only sends commits. It does not commit file changes for you.

## Checklist

### 1. Start by pulling the latest changes

Before making your own change, get the latest work from GitHub:

```bash
git pull
```

- [ ] I pulled the latest changes from GitHub.

### 2. Make a small SQL-related change

Edit a file such as:

```text
queries/01-count-visits.sql
```

For practice, add a comment that explains the query:

```sql
-- Count total visits in the starter data.
```

- [ ] I made one small file change.

### 3. Check status and diff

Run:

```bash
git status
git diff
```

Git should show that a file changed, and `git diff` should show the exact lines.

- [ ] I can see my changed file.
- [ ] I reviewed the exact change.
- [ ] I understand that an uncommitted file change will not be pushed.

### 4. Stage and commit the change

Stage the file:

```bash
git add queries/01-count-visits.sql
```

Commit the staged change:

```bash
git commit -m "docs: clarify visit count query"
```

- [ ] I staged my changed file.
- [ ] I committed the change.

### 5. Confirm you have a commit to push

Run:

```bash
git status
```

Git may say your branch is ahead of `origin/main` by one commit. That means you have a local commit that GitHub does not have yet.

- [ ] I know whether I have local commits to push.

### 6. Push your commit

Run:

```bash
git push
```

If this is the first push on a new branch, Git may ask you to use:

```bash
git push -u origin branch-name
```

- [ ] My commit was pushed to GitHub.

### 7. Confirm on GitHub

- [ ] I opened the repository in GitHub.
- [ ] I can see my change or commit.

## Important beginner habit

Before starting work each day, run:

```bash
git pull
```

Before and after each major step, run:

```bash
git status
```

Before staging, run:

```bash
git diff
```

## Completion check

- [ ] I can push commits to GitHub.
- [ ] I can pull changes from GitHub.
- [ ] I understand that push sends committed work up.
- [ ] I understand that pull brings GitHub changes down.
