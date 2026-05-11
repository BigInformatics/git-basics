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

### 1. Start by pulling the latest changes

Before making your own change, get the latest work from GitHub:

```bash
git pull
```

- [ ] I pulled the latest changes from GitHub.

### 2. Make a small change

Edit a file, such as `README.md`.

For practice, add one short sentence like:

```markdown
Practicing push and pull.
```

- [ ] I made one small file change.

### 3. Check status

Run:

```bash
git status
```

Git should show that a file has changed.

Important: a changed file is not ready to push yet. `git push` only sends commits to GitHub. It does not commit file changes for you.

- [ ] I can see my changed file.
- [ ] I understand that an uncommitted file change will not be pushed.

### 4. Stage and commit the change

Stage the file:

```bash
git add README.md
```

Replace `README.md` with the file you changed.

Commit the staged change:

```bash
git commit -m "docs: practice pushing a commit"
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

## Completion check

- [ ] I can push commits to GitHub.
- [ ] I can pull changes from GitHub.
- [ ] I understand that push sends changes up.
- [ ] I understand that pull brings changes down.
