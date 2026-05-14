# Lesson 03 — Cloning a Repository

## Goal

Copy a GitHub repository to your computer and confirm that Git can see it correctly.

![Concept card showing a GitHub repository copied into a local folder with files, history, and the origin connection.](/git-basics/images/git-lesson03-concept-cloning-a-repository.png)

## What cloning means

To **clone** a repository means to download a full working copy from GitHub to your computer.

After cloning, you have:

![Diagram showing git clone copying a GitHub repository into a local folder on your computer, including project files, Git history, and the origin connection back to GitHub.](/git-basics/images/git-clone-mental-model.svg)

- The project files
- The Git history
- A connection back to the GitHub repository

For this course, learners should work in their own copy of a practice template such as `git-basics-sql-practice`.

## Recommended practice setup

If the template repository is available:

1. Open the facilitator-provided template repository. The intended public template name is `BigInformatics/git-basics-sql-practice`.
2. Click **Use this template**.
3. Create a new repository under your own GitHub account or training organization.
4. Clone your new repository, not the course site.

This keeps practice work separate from the course materials.

## Checklist

### 1. Find the repository on GitHub

- [ ] Open your learner-owned practice repository in GitHub.
- [ ] Click the green **Code** button.
- [ ] Copy the HTTPS URL.

It will look like:

```text
https://github.com/your-account/git-basics-sql-practice.git
```

### 2. Choose where to put the project

In your terminal, move to a folder where you keep projects.

Example:

```bash
cd Documents
```

### 3. Clone the repository

Run:

```bash
git clone https://github.com/your-account/git-basics-sql-practice.git
```

Replace the URL with the actual repository URL.

- [ ] The repository downloaded successfully.

### 4. Move into the repository folder

Run:

```bash
cd git-basics-sql-practice
```

- [ ] I am now inside the repository folder.

### 5. Check status

Run:

```bash
git status
```

Expected result:

```text
On branch main
nothing to commit, working tree clean
```

The wording may vary slightly. The important points are that you are on a branch and Git does not show unexpected changes.

- [ ] Git says I am on a branch, usually `main`.
- [ ] Git says my working tree is clean.

### 6. Confirm the GitHub connection

Run:

```bash
git remote -v
```

You should see the GitHub URL for your learner-owned practice repository.

- [ ] `origin` points to my practice repository.

## Completion check

- [ ] I can clone a repository.
- [ ] I can move into the repository folder.
- [ ] I can run `git status` inside the repository.
- [ ] I can run `git remote -v` to see the GitHub connection.
- [ ] I know whether I am working in my practice repository or the course site.
