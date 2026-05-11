# Lesson 05 — Pushing and Pulling

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

## Checklist

### 1. Confirm you have a commit to push

Run:

```bash
git status
```

Git may say your branch is ahead of `origin/main` by one commit. That means you have local work that GitHub does not have yet.

- [ ] I know whether I have local commits to push.

### 2. Push your commit

Run:

```bash
git push
```

If this is the first push on a new branch, Git may ask you to use:

```bash
git push -u origin branch-name
```

- [ ] My commit was pushed to GitHub.

### 3. Confirm on GitHub

- [ ] I opened the repository in GitHub.
- [ ] I can see my change or commit.

### 4. Pull updates

Before starting work, get the latest changes:

```bash
git pull
```

- [ ] I pulled the latest changes from GitHub.

## Important beginner habit

Before starting work each day, run:

```bash
git pull
```

Before and after each major step, run:

```bash
git status
```

## Completion check

- [ ] I can push commits to GitHub.
- [ ] I can pull changes from GitHub.
- [ ] I understand that push sends changes up.
- [ ] I understand that pull brings changes down.
