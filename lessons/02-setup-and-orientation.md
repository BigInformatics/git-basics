# Lesson 02 — Setup and First Orientation

## Goal

Confirm Git is installed and configured with your name and email.

## Checklist

### 1. Confirm Git is installed

Run:

```bash
git --version
```

- [ ] I saw a Git version number.

If Git is not installed, ask your technical support contact or install Git from <https://git-scm.com/>.

### 2. Configure your name

Run:

```bash
git config --global user.name "Your Name"
```

- [ ] I configured my name.

### 3. Configure your email

Use the email associated with your GitHub account when possible.

```bash
git config --global user.email "you@example.com"
```

- [ ] I configured my email.

### 4. Confirm your Git settings

Run:

```bash
git config --global --list
```

- [ ] I can see my `user.name`.
- [ ] I can see my `user.email`.

## Important habit

`git status` is the most important beginner command. It tells you where you are and what Git sees.

You will use it constantly.

## Practice task

Run:

```bash
git status
```

If you are not inside a repository yet, Git may say something like:

```text
fatal: not a git repository
```

That is okay. It just means you are not inside a Git-tracked project folder yet.

## Completion check

- [ ] Git is installed.
- [ ] My name is configured.
- [ ] My email is configured.
- [ ] I know that `git status` tells me what Git sees.
