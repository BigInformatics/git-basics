# Lesson 04 — Status, Staging, and Commits

## Goal

Make a small file change and save it in Git history as a commit.

## Core workflow

```text
edit → status → add → commit → status
```

## What these commands mean

```bash
git status
```

Shows what changed.

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

### 2. Make a small change

Edit a file, such as `README.md`.

Example change:

```markdown
Practicing Git basics.
```

- [ ] I made one small file change.

### 3. Check status again

Run:

```bash
git status
```

- [ ] I can see the changed file listed.

### 4. Stage the changed file

Run:

```bash
git add README.md
```

Replace `README.md` with the file you changed.

- [ ] I staged the file.

### 5. Check status again

Run:

```bash
git status
```

- [ ] I can see that the change is staged.

### 6. Commit the change

Run:

```bash
git commit -m "docs: practice a README change"
```

- [ ] I created a commit.

### 7. Check status one more time

Run:

```bash
git status
```

- [ ] Git says there is nothing to commit.

## Good commit messages

A good commit message is short and specific.

Examples:

```text
docs: update README instructions
fix: correct typo in analysis notes
chore: add project folder structure
```

## Completion check

- [ ] I can make a small change.
- [ ] I can stage a change with `git add`.
- [ ] I can commit a change with `git commit`.
- [ ] I understand that commits are local until pushed.
