---
title: 'Practice Checklist'
sidebar:
  order: 2
---

Use this checklist inside a learner-owned copy of a practice template, preferably `git-basics-sql-practice`.

The same pattern should be repeated several times with small changes. The objective is comfort with the workflow, not speed.

## Before each round

```bash
git checkout main
git pull
git status
```

- [ ] I am on `main`.
- [ ] My local copy is up to date.
- [ ] `git status` does not show leftover changes from another exercise.

## Round 1 — Edit an analysis note

- [ ] Create a branch named `docs/add-analysis-note`.
- [ ] Open `analysis-notes/findings.md`.
- [ ] Add one short note about what the starter query is intended to answer.
- [ ] Run `git status`.
- [ ] Run `git diff` and review the exact text I changed.
- [ ] Stage the file.
- [ ] Commit with `docs: add analysis note`.
- [ ] Push the branch.
- [ ] Open a pull request.
- [ ] Merge it after review.
- [ ] Switch back to `main` and pull the merged change.

## Round 2 — Update a SQL query comment

- [ ] Create a branch named `analysis/clarify-visit-query`.
- [ ] Open `queries/01-count-visits.sql`.
- [ ] Add or improve a comment that explains what the query counts.
- [ ] Run `git status`.
- [ ] Run `git diff`.
- [ ] Stage only the SQL file.
- [ ] Commit with `docs: clarify visit count query`.
- [ ] Push the branch.
- [ ] Open a pull request.
- [ ] Update the PR if feedback is requested.
- [ ] Merge the PR and pull the latest `main`.

## Round 3 — Improve a data dictionary entry

- [ ] Create a branch named `metadata/define-visit-date`.
- [ ] Open `data-dictionary/patient_visits.md`.
- [ ] Add or revise one field definition.
- [ ] Run `git status`.
- [ ] Run `git diff`.
- [ ] Stage the data dictionary file.
- [ ] Commit with `docs: define visit date field`.
- [ ] Push the branch.
- [ ] Open a pull request.
- [ ] Merge the PR after review.
- [ ] Pull the latest `main`.

## Round 4 — Practice responding to PR feedback

Use the same branch if a reviewer asks for a correction.

- [ ] Make the requested change locally.
- [ ] Run `git status`.
- [ ] Run `git diff`.
- [ ] Stage the correction.
- [ ] Commit with `docs: address review feedback`.
- [ ] Push again.
- [ ] Confirm the existing PR updated automatically.

## Reflection questions

- [ ] What command tells you what Git sees right now?
- [ ] What command shows the exact text changed before staging?
- [ ] What command saves a local checkpoint?
- [ ] What command sends committed work to GitHub?
- [ ] What command brings GitHub changes down to your computer?
- [ ] Why do we use branches for small changes?
- [ ] Why do we use pull requests before merging?
