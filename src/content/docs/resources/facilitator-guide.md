---
title: 'Facilitator Guide'
sidebar:
  order: 3
---

## Purpose

This guide supports a hands-on Git/GitHub onboarding session for analysts and statisticians.

The primary goal is confidence through repetition, not comprehensive Git knowledge.

## Recommended session structure

### Session 1 — Orientation and first commit

Time: 45–60 minutes

1. Explain Git vs GitHub using the local/remote model.
2. Confirm everyone has Git installed.
3. Confirm everyone can access GitHub.
4. Clone a practice repository.
5. Make one small README change.
6. Stage and commit the change.
7. Push the change.

### Session 2 — Branches and pull requests

Time: 45–60 minutes

1. Start from an updated `main` branch.
2. Create a new branch.
3. Make a small change.
4. Commit and push the branch.
5. Open a pull request.
6. Review one another's PRs.
7. Merge the PR.
8. Pull the updated `main` branch.

### Session 3 — Repetition and troubleshooting

Time: 45–60 minutes

1. Repeat the full workflow with a new small change.
2. Practice reading `git status` together.
3. Practice identifying the current branch.
4. Practice updating a PR after feedback.
5. Discuss safe commands and commands to ask about first.

## Facilitation tips

- Have learners type the commands themselves.
- Use very small file changes.
- Pause after every command and ask: "What did Git say?"
- Normalize mistakes. Most Git learning comes from recovering calmly.
- Encourage learners to run `git status` whenever they feel uncertain.
- Avoid introducing advanced topics too early.

## Common beginner sticking points

### Authentication problems

Symptoms:

- Git asks for a password.
- Push fails.
- GitHub says permission denied.

Response:

- Confirm the learner is logged in to GitHub.
- Confirm they have access to the repository.
- Use GitHub's recommended authentication method for the environment.

### Wrong folder

Symptom:

```text
fatal: not a git repository
```

Response:

- The learner is probably not inside the repository folder.
- Have them locate the cloned folder and `cd` into it.

### Wrong branch

Symptom:

- The learner made changes on `main` instead of a branch.

Response:

- Do not panic.
- Check `git status`.
- If changes are uncommitted, create a branch before committing:

```bash
git checkout -b branch-name
```

### Nothing to commit

Symptom:

```text
nothing to commit, working tree clean
```

Response:

- Git does not currently see any unsaved changes.
- Confirm the file was saved in the editor.
- Confirm the learner is in the expected repository.

## What not to teach on day one

Avoid these until learners are comfortable with the basic workflow:

- Rebase
- Cherry-pick
- Reset hard
- Force push
- Merge conflict internals
- Complex branching strategies

## Success criteria

A learner is ready for normal beginner use when they can complete this without prompting:

```text
pull main → create branch → edit file → status → add → commit → push → open PR
```
