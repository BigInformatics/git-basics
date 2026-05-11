---
title: 'Lesson 03 — Cloning a Repository'
sidebar:
  order: 3
---

## Goal

Copy an existing GitHub repository to your computer.

## What cloning means

To **clone** a repository means to download a full working copy of it from GitHub to your computer.

After cloning, you have:

- The project files
- The Git history
- A connection back to the GitHub repository

## Checklist

### 1. Find the repository on GitHub

- [ ] Open the repository page in GitHub.
- [ ] Click the green **Code** button.
- [ ] Copy the HTTPS URL.

It will look like:

```text
https://github.com/organization/repository-name.git
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
git clone https://github.com/organization/repository-name.git
```

Replace the URL with the actual repository URL.

- [ ] The repository downloaded successfully.

### 4. Move into the repository folder

Run:

```bash
cd repository-name
```

- [ ] I am now inside the repository folder.

### 5. Check status

Run:

```bash
git status
```

- [ ] Git says I am on a branch, usually `main`.
- [ ] Git says my working tree is clean.

## Practice task

Clone a practice repository, enter the folder, and run:

```bash
git status
git remote -v
```

`git remote -v` shows the GitHub address connected to your local copy.

## Completion check

- [ ] I can clone a repository.
- [ ] I can move into the repository folder.
- [ ] I can run `git status` inside the repository.
- [ ] I can run `git remote -v` to see the GitHub connection.
