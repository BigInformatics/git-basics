---
title: 'Template Practice Repositories'
sidebar:
  order: 1
---

Use template repositories when learners need their own safe copy of a project.

A template repository lets each learner create a new repository from the same starting files. They can branch, commit, push, open pull requests, and merge without changing the course site or another learner's work.

## Recommended template set

Start with one template. Add more only when the course needs a different practice context.

| Template repository | Purpose | Example learner tasks |
| --- | --- | --- |
| [`git-basics-sql-practice`](https://github.com/BigInformatics/git-basics-sql-practice) | SQL analysis workflow | edit a query, add notes, update a data dictionary, open a PR |
| `git-basics-docs-practice` | Documentation-only workflow | fix a typo, improve instructions, respond to PR feedback |
| `git-basics-data-dictionary-practice` | Metadata workflow | add a field definition, review naming, update source notes |

The first build should use [`git-basics-sql-practice`](https://github.com/BigInformatics/git-basics-sql-practice). It is realistic enough for analysts and statisticians without requiring live database credentials.

## Structure for [`git-basics-sql-practice`](https://github.com/BigInformatics/git-basics-sql-practice)

```text
git-basics-sql-practice/
├── README.md
├── queries/
│   ├── 01-count-visits.sql
│   └── 02-enrollment-summary.sql
├── data-dictionary/
│   └── fields.md
├── analysis-notes/
│   └── visit-count-notes.md
└── troubleshooting/
    └── common-issues.md
```

Keep the repository small. The goal is Git practice, not SQL mastery.

## What should be in the template

- Small SQL files that can be read without a database connection.
- Data dictionary markdown files with realistic field names.
- Analysis notes where learners can write short observations.
- A `README.md` with expected workflow and branch naming examples.
- No connection strings, credentials, private hostnames, or real client data.

## Learner setup flow

Each learner creates their own repository from the template:

1. Open [BigInformatics/git-basics-sql-practice](https://github.com/BigInformatics/git-basics-sql-practice).
2. Select **Use this template**.
3. Create a repository under their own account or training organization.
4. Clone their new repository.
5. Complete the course exercises in that copy.


## Naming convention

Use the `git-basics-` prefix for every practice template so repositories appear together in GitHub search and organization lists.

Good examples:

```text
git-basics-sql-practice
git-basics-docs-practice
git-basics-data-dictionary-practice
```

Avoid vague names such as `practice-repo` or `training-files`.
