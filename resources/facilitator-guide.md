# Facilitator Guide

## Purpose

This guide supports hands-on Git/GitHub onboarding for analysts, statisticians, epidemiologists, evaluators, and public health data staff.

The primary goal is confidence through repetition, not comprehensive Git knowledge. Learners may be adopting Git during high workload and reduced staffing; facilitation should reduce uncertainty, not add performance pressure.

## Facilitator stance

Use a calm, practical tone.

- Treat `git status` as the shared source of truth.
- Ask “What does Git say?” before explaining what to do.
- Keep examples tied to ordinary analysis work: SQL comments, data dictionaries, findings notes, scripts, and reports.
- Use small changes so the Git workflow is the focus.
- Avoid jokes about breaking things, magical metaphors, mascots, or “Git superpowers.”

## The four questions to reinforce

| Question | Where learners look |
| --- | --- |
| What does Git know? | `git status`, `git diff`, `git diff --staged` |
| What does GitHub have? | repository page, branch page, pull request page |
| What changed? | diff output and PR Files changed tab |
| What happens next? | checklist step, status message, PR review state |

Use the [GitHub Basics infographic](/git-basics/resources/github-basics-infographic/) as a shared visual map throughout the course. It gives learners a stable picture of where each command fits in the collaboration loop.

## Recommended session structure

### Session 1 — Orientation and first commit

Time: 45–60 minutes

1. Open the GitHub Basics infographic and preview the full collaboration loop.
2. Explain Git vs GitHub using the local/remote model.
3. Confirm everyone has Git installed.
4. Confirm everyone can access GitHub.
5. Clone a practice repository.
6. Make one small analysis-note change.
7. Run `git status` and `git diff` together.
8. Stage and commit the change.
9. Emphasize: the commit is local until pushed.
10. Push the commit if using a learner-owned repo.

### Session 2 — Branches and pull requests

Time: 45–60 minutes

1. Revisit the infographic and name the steps learners practiced last time.
2. Start from an updated `main` branch.
3. Create a new branch.
4. Make a small SQL comment or data dictionary change.
5. Run `git status`, `git diff`, and `git diff --staged`.
6. Commit and push the branch.
7. Open a pull request.
8. Review one another's PRs using the Files changed tab.
9. Merge the PR.
10. Pull the updated `main` branch.

### Session 3 — Repetition and troubleshooting

Time: 45–60 minutes

1. Repeat the full workflow with a new small change.
2. Practice reading `git status` together.
3. Practice identifying the current branch.
4. Practice updating a PR after feedback.
5. Discuss safe commands and commands to ask about first.

## Board-friendly diagram

```text
Learner computer                                 GitHub
----------------                                 ------
working files → stage → local commit → push → branch on GitHub → pull request → main
       ↑                         │                                      │
       └──── status/diff checks ─┘                                      └─ pull back to local main
```

## Facilitation tips

- Have learners type the commands themselves.
- Use very small file changes.
- Pause after every command and ask: “What did Git say?”
- Normalize mistakes without dramatizing them. Most Git learning comes from recovering calmly.
- Encourage learners to run `git status` whenever they feel uncertain.
- Avoid introducing advanced topics too early.
- Do not let one fast learner set the pace for the room.
- Make time for learners to compare the terminal, GitHub, and their editor.

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
- Avoid troubleshooting credentials in front of the full room if sensitive information may appear.

### Wrong folder

Symptom:

```text
fatal: not a git repository
```

Response:

- The learner is probably not inside the repository folder.
- Have them locate the cloned folder and `cd` into it.
- Then run `git status` again.

### Wrong branch

Symptom:

- The learner made changes on `main` instead of a branch.

Response:

- Do not panic.
- Check `git status`.
- If changes are uncommitted, create a branch before committing:

```bash
git switch -c branch-name
```

or:

```bash
git checkout -b branch-name
```

### Nothing to commit

Symptom:

```text
nothing to commit, working tree clean
```

Response:

- Git does not currently see any uncommitted file changes.
- Confirm the file was saved in the editor.
- Confirm the learner edited the expected repository.
- If a commit was just made, this message may mean the working tree is clean and the next step is push.

### Push did not include my file

Likely cause:

- The learner edited or staged a file but did not commit it.

Response:

- Re-state the model: `git push` sends commits only.
- Run `git status`.
- If changes are unstaged or staged, review, commit, then push.

### PR does not update after feedback

Likely causes:

- The learner committed on a different branch.
- The learner committed locally but did not push.

Response:

- Run `git status` and check the branch name.
- If the branch is ahead, run `git push`.
- Confirm the PR source branch matches the learner's branch.

## What not to teach on day one

Avoid these until learners are comfortable with the basic workflow:

- Rebase
- Cherry-pick
- Reset hard
- Force push
- Merge conflict internals
- Complex branching strategies
- Stash, unless there is a concrete need

## Success criteria

A learner is ready for normal beginner use when they can complete this without prompting:

```text
pull main → create branch → edit file → status → diff → add → commit → push → open PR
```

They should also be able to say:

- `git status` tells me what Git knows right now.
- `git diff` tells me what changed.
- `git commit` saves a local checkpoint.
- `git push` sends commits to GitHub; it does not commit file changes.
- A pull request is where the team reviews before merging to `main`.
