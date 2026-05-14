# Lesson 04 — Status, Staging, and Commits

## Goal

Make one small change in the practice repository, inspect what changed, and save it in Git history as a commit.

This lesson is deliberately slow. The skill is not typing commands quickly; the skill is knowing what Git knows before you move to the next step.

## Mental model

![Diagram showing work moving from the working tree, to the staging area with git add, and then to local Git history with git commit.](/git-basics/images/git-three-places.svg)

```text
Your files on disk          Staging area              Local Git history
------------------          ------------              -----------------
working tree       --add-->  next commit     --commit--> saved checkpoint
```

Git tracks three useful questions:

| Question | Command | What you learn |
| --- | --- | --- |
| What does Git see right now? | `git status` | Branch, changed files, staged files, and next-step hints |
| What exactly changed? | `git diff` | Line-by-line unstaged edits |
| What is ready to be committed? | `git diff --staged` | Line-by-line staged edits |

> **Calm habit:** Run `git status` whenever you feel unsure. It is a diagnostic command, not a test.

## Core workflow

![Diagram of the Lesson 04 core workflow: edit, status, diff, add, status, diff staged, commit, and status again to confirm the result.](/git-basics/images/git-lesson04-core-workflow.svg)

```text
edit → status → diff → add → status → diff --staged → commit → status
```

## What these commands mean

```bash
git status
```

Shows what Git knows about your working tree, staging area, current branch, and relationship to GitHub.

```bash
git diff
```

Shows the exact text changes that are not staged yet.

```bash
git add filename
```

Stages a file. Staging means: "include this version of this file in my next commit."

```bash
git diff --staged
```

Shows the exact text changes currently staged for the next commit.

```bash
git commit -m "message"
```

Creates a saved checkpoint in local Git history.

> **Important:** A commit is local until you push it. A push sends commits to GitHub; it does not create commits from unsaved file changes.

## Checklist

### 1. Start clean

Run:

```bash
git status
```

Expected if nothing is pending:

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

If Git lists changes, pause and decide whether they belong to this exercise before continuing.

- [ ] I know which branch I am on.
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

Save the file in your editor.

- [ ] I made one small file change.
- [ ] I saved the file.

### 3. Check status again

Run:

```bash
git status
```

Expected shape:

```text
Changes not staged for commit:
  modified:   analysis-notes/findings.md
```

This means Git sees a saved file change, but the change is not staged yet.

- [ ] I can see the changed file listed.
- [ ] I understand this change is not committed yet.

### 4. Review the exact change

Run:

```bash
git diff
```

Read the output before staging. Look for your new line and check that no unrelated edits appear.

Diffs use a consistent pattern:

```text
- lines removed from the file
+ lines added to the file
```

- [ ] I reviewed the exact lines I changed.
- [ ] I do not see unrelated edits.

### 5. Stage the changed file

Run:

```bash
git add analysis-notes/findings.md
```

- [ ] I staged the file.

### 6. Check what is staged

Run:

```bash
git status
git diff --staged
```

Expected shape from `git status`:

```text
Changes to be committed:
  modified:   analysis-notes/findings.md
```

`git diff --staged` should show the same intentional change you reviewed earlier.

- [ ] I can see that the change is staged.
- [ ] I reviewed what will go into the commit.

### 7. Commit the change

Run:

```bash
git commit -m "docs: add analysis note"
```

Expected shape:

```text
[main abc1234] docs: add analysis note
 1 file changed, 1 insertion(+)
```

The identifier will be different on your computer.

- [ ] I created a local commit.

### 8. Check status one more time

Run:

```bash
git status
```

Expected shape:

```text
nothing to commit, working tree clean
```

If Git says your branch is ahead of `origin/main` by one commit, that is also useful information: your commit exists locally and has not been pushed to GitHub yet.

- [ ] Git says there is nothing to commit.
- [ ] I know whether this local commit still needs to be pushed.

## Good commit messages

A good commit message is short, specific, and written for the next person who reviews the history.

| Less helpful | More helpful |
| --- | --- |
| `updates` | `docs: add analysis note` |
| `fix stuff` | `docs: clarify visit count query` |
| `changes` | `fix: correct county label typo` |

More examples:

```text
docs: add analysis note
docs: clarify visit count query
docs: define visit date field
fix: correct county label typo
```

## If something looks wrong

| Situation | Safe next step |
| --- | --- |
| You changed the wrong file | Do not stage yet. Ask for help or use your editor to undo the file. |
| `git diff` is empty but you expected changes | Save the file and check you are in the right repository. |
| You staged too much | Ask for help before using reset commands. |
| You are not sure what happened | Run `git status` and read the branch and file sections aloud. |

## Completion check

- [ ] I can make a small change.
- [ ] I can review the change with `git diff`.
- [ ] I can stage a specific file with `git add filename`.
- [ ] I can review staged work with `git diff --staged`.
- [ ] I can commit a change with `git commit`.
- [ ] I understand that commits are local until pushed.
