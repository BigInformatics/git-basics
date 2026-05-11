---
title: 'Lesson 07 — Pull Requests'
sidebar:
  order: 7
---

## Goal

Open a pull request so someone can review your branch before it is merged.

## What a pull request is

A **pull request**, or **PR**, is a request to merge one branch into another branch.

Most often:

```text
your branch → main
```

A PR gives the team a place to:

- Review changes
- Ask questions
- Suggest edits
- Run automated checks
- Approve and merge work

## Checklist

### 1. Push your branch

Make sure your branch is on GitHub:

```bash
git push -u origin branch-name
```

- [ ] My branch is pushed to GitHub.

### 2. Open the repository in GitHub

- [ ] I opened the repository page.
- [ ] I see my recently pushed branch.

### 3. Start the pull request

- [ ] Click **Compare & pull request**, or go to the **Pull requests** tab and click **New pull request**.
- [ ] Confirm the base branch is `main`.
- [ ] Confirm the compare branch is my branch.

### 4. Write a clear PR title

Example:

```text
docs: add practice notes to README
```

- [ ] My PR title clearly says what changed.

### 5. Fill in the PR description

Use this template:

```markdown
## Summary
- 
- 

## Testing or review notes
- [ ] I reviewed the changed files
- [ ] I ran `git status`
- [ ] I confirmed the change appears as expected
```

- [ ] I wrote a short PR description.

### 6. Create the PR

- [ ] I clicked **Create pull request**.

### 7. Respond to feedback

If someone asks for a change:

1. Make the change locally on the same branch.
2. Commit it.
3. Push it.

```bash
git add filename
git commit -m "docs: address PR feedback"
git push
```

The PR updates automatically.

- [ ] I understand how to update a PR.

## Completion check

- [ ] I can open a PR.
- [ ] I can explain what branch is being merged into what branch.
- [ ] I can update a PR by pushing another commit to the same branch.
- [ ] I understand that PRs are for review and discussion.
