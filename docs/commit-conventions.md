# Commit Conventions

> :uk: English | [:hungary: Magyar](README.hu.md)

**Purpose**: Standardize commit messages for better readability and project history tracking.

---

## Formats & Examples

### Simple Format

```plaintext
<type>(<scope>): <short summary>
```

```bash
docs: correct spelling of CHANGELOG
```

### Conventional Commit Format

```plaintext
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

```bash
feat(auth): add user login endpoint

- Implement POST /login endpoint
- Add JWT token generation
- Update user model validation

Closes #45
```

### Example Bash Command

```bash
git commit -m "feat(auth): add user login endpoint" \
  -m "- Implement POST /login endpoint\n" \
  -m "- Add JWT token generation\n" \
  -m "- Update user model validation\n\n" \
  -m "Closes #45"
```

---

## Commit Types & Scope

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, whitespace)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks (e.g., updating dependencies)

> **Scope**: Specific module, component, or area affected (e.g., `auth`, `ui`, `api`)

---

## Commit Message Structure

### Description

- Short, clear summary of changes (50 characters or less)

### Body (Optional)

- Detailed explanation of the change
- Use bullet points for clarity
- Explain *what* changed and *why*

### Footer (Optional)

- Reference issues or pull requests (e.g., `Closes #123`)
- Breaking changes: `BREAKING CHANGE: <description>`

---

## Revert Commits

- Use the `revert:` type for revert commits.

  Example:

  ```plaintext
  revert: let us never again speak of the noodle incident

  Refs: 676104e, a215868
  ```

  Example Bash Command:

  ```bash
  git revert <commit-hash>
  # Example: git revert 676104e
  ```

  > Tip: If you use the wrong commit type, you can fix it with `git rebase -i` before merging or releasing.

---

## Tips, Casing, Best Practices

- Commit types are not case sensitive, but use consistent casing.
- Write clear, concise messages
- Use present tense (e.g., "add feature" not "added feature")
- Keep line length under 72 characters
- Separate subject from body with a blank line
- If a commit lands with a non-standard type, tooling may ignore it, but it's not critical.
- Not all contributors must use the spec; maintainers can clean up messages during squash merges.
- If a commit fits more than one type, split it into multiple commits for clarity.

---

## Git Hook Script

To automatically enforce Conventional Commit message formats on your repository, you can use a server-side git hook:

Create the following file in your repository folder as `.git/hooks/pre-receive`:

```bash
#!/usr/bin/env bash

# Pre-receive hook that will block commits with messages that do not follow regex rule
commit_msg_type_regex='feat|fix|refactor|style|test|docs|build'
commit_msg_scope_regex='.{1,20}'
commit_msg_description_regex='.{1,100}'
commit_msg_regex="^(${commit_msg_type_regex})(\(${commit_msg_scope_regex}\))?: (${commit_msg_description_regex})$"
merge_msg_regex="^Merge branch '.+'$"

zero_commit="0000000000000000000000000000000000000000"
excludeExisting="--not --all"
error=""

while read oldrev newrev refname; do
    if [ "$newrev" = "$zero_commit" ]; then
      continue
    fi
    if [ "$oldrev" = "$zero_commit" ]; then
      rev_span=`git rev-list $newrev $excludeExisting`
    else
      rev_span=`git rev-list $oldrev..$newrev $excludeExisting`
    fi
    for commit in $rev_span; do
      commit_msg_header=$(git show -s --format=%s $commit)
      if ! [[ "$commit_msg_header" =~ (${commit_msg_regex})|(${merge_msg_regex}) ]]; then
        echo "$commit" >&2
        echo "ERROR: Invalid commit message format" >&2
        echo "$commit_msg_header" >&2
        error="true"
      fi
    done
done

if [ -n "$error" ]; then
    exit 1
fi
```

Make the hook executable:

```bash
chmod +x .git/hooks/pre-receive
```

---

## Sources

- [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
- [Git Commit Guidelines](https://github.com/angular/angular/blob/main/CONTRIBUTING.md#commit)
- [Conventional Commit Messages](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13)

---

*Last updated at: 2025.08.02.*
