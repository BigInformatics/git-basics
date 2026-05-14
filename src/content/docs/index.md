---
title: Git Basics for Analysts and Statisticians
description: A hands-on Git and GitHub course for public health data teams.
template: splash
hero:
  tagline: Learn Git through small repeatable workflows—not long lectures.
  actions:
    - text: Start Lesson 01
      link: /git-basics/lessons/01-what-git-and-github-are/
      icon: right-arrow
    - text: Practice Checklist
      link: /git-basics/exercises/practice-checklist/
      variant: secondary
    - text: Template Repositories
      link: /git-basics/practice/template-repositories/
      variant: secondary
    - text: GitHub Basics Infographic
      link: /git-basics/resources/github-basics-infographic/
      variant: secondary
---

## What this site teaches

This site helps analysts, statisticians, epidemiologists, evaluators, and public health data teams practice the Git and GitHub workflow they need for everyday collaboration.

It is built for people adopting Git while real work is still moving: reports are due, staffing is tight, and nobody needs extra drama from their tools. The course uses small, repeatable tasks so learners can build calm working habits.

```text
start updated → branch → edit → inspect → stage → commit → push → PR → update main
```

## The core mental model

```text
Your computer                                           GitHub
-------------                                           ------
working files → staging area → local commits  → push →  shared commits
                                      shared commits ← pull ← reviewed work
```

| Learner question | Git/GitHub idea | Command or place to check |
| --- | --- | --- |
| What does Git know right now? | Current branch, file changes, staged work | `git status` |
| What changed? | Line-by-line edits | `git diff` and `git diff --staged` |
| What has been saved locally? | Commits on your computer | `git log --oneline` |
| What does GitHub have? | Pushed branches, commits, and pull requests | Repository page on GitHub |
| What happens next? | Pull, branch, stage, commit, push, or open/review a PR | The lesson checklists |

> **Important course promise:** Git becomes manageable when you can answer four questions: what Git knows, what GitHub has, what changed, and what happens next.

## What learners will practice

- Cloning a repository from GitHub.
- Reading `git status` before acting.
- Reviewing changes with `git diff`.
- Staging specific files.
- Making clear local commits.
- Understanding that `git push` sends commits; it does not commit file changes.
- Pulling updates from GitHub.
- Creating branches for small changes.
- Opening, updating, reviewing, and merging pull requests.

## Recommended path

| Phase | Lessons | Outcome |
| --- | --- | --- |
| Orientation | Lessons 01–03 | Know what Git and GitHub are, install/check tools, clone a practice repo |
| Local workflow | Lesson 04 | Edit, inspect, stage, and commit locally |
| Sharing work | Lesson 05 | Pull from GitHub and push committed work |
| Collaboration | Lessons 06–07 | Use branches and pull requests |
| Repetition | Lesson 08 + checklist | Complete the full workflow several times |

## Quick visual reference

Start with the [GitHub Basics infographic](/git-basics/resources/github-basics-infographic/) to see the whole safe collaboration loop at once.

![GitHub Basics infographic showing the safe collaboration loop from branch to pull request to review and merge.](/git-basics/images/github-basics-infographic.png)

## Lessons

1. [What Git and GitHub Are](/git-basics/lessons/01-what-git-and-github-are/)
2. [Setup and First Orientation](/git-basics/lessons/02-setup-and-orientation/)
3. [Cloning a Repository](/git-basics/lessons/03-cloning-a-repository/)
4. [Status, Staging, and Commits](/git-basics/lessons/04-status-staging-commits/)
5. [Pushing and Pulling](/git-basics/lessons/05-pushing-and-pulling/)
6. [Branching](/git-basics/lessons/06-branching/)
7. [Pull Requests](/git-basics/lessons/07-pull-requests/)
8. [A Complete Beginner Workflow](/git-basics/lessons/08-complete-workflow/)

## Practice and resources

- [Practice Checklist](/git-basics/exercises/practice-checklist/)
- [Template Practice Repositories](/git-basics/practice/template-repositories/)
- [GitHub Basics Infographic](/git-basics/resources/github-basics-infographic/)
- [Command Cheat Sheet](/git-basics/resources/command-cheat-sheet/)
- [Glossary](/git-basics/resources/glossary/)
- [Facilitator Guide](/git-basics/resources/facilitator-guide/)
