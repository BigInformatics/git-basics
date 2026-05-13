# Git Command Cheat Sheet

## Where am I?

```bash
git status
```

Shows changed files, staged files, branch name, and whether there is anything to commit.

## Download a repository

```bash
git clone https://github.com/organization/repository-name.git
```

Copies a GitHub repository to your computer.

## See the GitHub connection

```bash
git remote -v
```

Shows the remote repository URL.

## Bring down the latest work

```bash
git pull
```

Gets the latest commits from GitHub.

## Create a branch

```bash
git checkout -b branch-name
```

or:

```bash
git switch -c branch-name
```

Creates and switches to a new branch.

## Switch branches

```bash
git checkout main
```

or:

```bash
git switch main
```

Switches to another branch.

## List branches

```bash
git branch
```

Shows local branches. The current branch has an asterisk.

## Stage a file

```bash
git add filename
```

Prepares a file for the next commit.

## Stage all current changes

```bash
git add .
```

Prepares all changed files in the current folder and below.

Use carefully. Beginners should often prefer staging specific files.

## Commit staged changes

```bash
git commit -m "short message"
```

Saves staged changes as a local checkpoint.

## Push a branch the first time

```bash
git push -u origin branch-name
```

Sends a new branch to GitHub and connects the local branch to the remote branch.

## Push after the first time

```bash
git push
```

Sends local commits to GitHub.

Important: `git push` sends commits only. It does not stage files, create commits, or send uncommitted edits.

## Check what will be committed

```bash
git diff --staged
```

Shows staged line-by-line changes before you commit.

## View commit history

```bash
git log
```

Shows previous commits.

For a shorter view:

```bash
git log --oneline
```

## Beginner safety commands

```bash
git status
```

Run this often.

```bash
git diff
```

Shows unstaged line-by-line changes.

```bash
git diff --staged
```

Shows staged line-by-line changes.

## Commands to ask for help before using

Beginners should ask for help before using:

```bash
git reset --hard
git push --force
git rebase
git clean -fd
```

These commands can discard work or rewrite history if used incorrectly.
