---
title: 'Lesson 04 — Status, Staging, and Commits'
sidebar:
  order: 4
---

## Goal

Make a small change in the practice repository and save it in Git history as a commit.

## Core workflow

```text
edit → status → diff → add → commit → status
```

Run `git status` often. It is the safest way to see what Git thinks is happening.

## What these commands mean

```bash
git status
```

Shows which files changed.

```bash
git diff
```

Shows the exact text changes that are not staged yet.

```bash
git add filename
```

Stages a file. Staging means: "include this in my next commit."

```bash
git commit -m "message"
```

Creates a saved checkpoint in Git history.

## Checklist

### 1. Start clean

Run:

```bash
git status
```

- [ ] I know whether my working tree is clean or has changes.

### 2. Make one small change

In `git-basics-sql-practice`, open:

```text
analysis-notes/findings.md
```

Add one short note about the question an analysis should answer.

Example:

```markdown
This query should help us confirm whether visit counts changed by county.
```

- [ ] I made one small file change.

### 3. Check status again

Run:

```bash
git status
```

- [ ] I can see the changed file listed.

### 4. Review the exact change

Run:

```bash
git diff
```

- [ ] I reviewed the exact lines I changed.
- [ ] I do not see unrelated edits.

### 5. Stage the changed file

Run:

```bash
git add analysis-notes/findings.md
```

- [ ] I staged the file.

### 6. Check status again

Run:

```bash
git status
```

- [ ] I can see that the change is staged.

### 7. Commit the change

Run:

```bash
git commit -m "docs: add analysis note"
```

- [ ] I created a commit.

### 8. Check status one more time

Run:

```bash
git status
```

- [ ] Git says there is nothing to commit.

## Good commit messages

A good commit message is short and specific.

Examples:

```text
docs: add analysis note
docs: clarify visit count query
docs: define visit date field
fix: correct county label typo
```

## Completion check

- [ ] I can make a small change.
- [ ] I can review the change with `git diff`.
- [ ] I can stage a change with `git add`.
- [ ] I can commit a change with `git commit`.
- [ ] I understand that commits are local until pushed.
