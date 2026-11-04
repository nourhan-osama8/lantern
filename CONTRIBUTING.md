# Contributing to Lantern

Thank you for contributing to Lantern!

This document describes the conventions followed by our team when contributing to the project.

## 1. Development Workflow

- Work on your own short-lived branch.
- Do not push changes directly to `main`.
- All changes must be submitted through Pull Requests.
- Keep each contribution focused on one task.

## 2. Branch Naming

Use descriptive branch names with the following prefixes:

- `feature/` – New features.
- `fix/` – Bug fixes.
- `docs/` – Documentation changes.

Examples:
- `feature/list-sort`
- `fix/empty-list`
- `docs/contributing`

## 3. Commit Messages

Follow the Conventional Commits format:

`type(scope): description`

We use the following commit types:

- `feat` – New features.
- `fix` – Bug fixes.
- `docs` – Documentation changes.
- `refactor` – Code improvements.
- `test` – Adding or updating tests.
- `chore` – Maintenance tasks.

Commit guidelines:

- Keep commit messages clear and descriptive.
- Keep the subject line within 50 characters whenever possible.
- Make one logical change per commit.
- Include a commit body explaining why the change was made when appropriate.

## 4. Pull Request Guidelines

- Create a Pull Request for every contribution.
- Use Conventional Commits format for the PR title.
- Explain what changed and why in the description.
- Reference the related issue using `Closes #issue-number`.
- Request a review from the other team member.
- Address requested changes and resolve review conversations.
- Merge only after receiving approval.
- Delete the branch after merging.

## 5. Code Guidelines

- Use Python 3.
- Use the Python standard library only.
- Keep changes simple and easy to review.
- Do not commit generated files, logs, private files, or `tasks.json`.
- Follow the repository's `.gitignore` rules.

Thank you for helping improve Lantern!
