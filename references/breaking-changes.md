# Breaking Changes & Multi-Line Commit Specifications

When a change introduces backwards-incompatible API or behavioral modifications, it MUST trigger a **MAJOR** version bump (`X.y.z`).

---

## 1. The Header Indicator (`!`)

To immediately signal a breaking change in single-line views (`git log --oneline`), append an exclamation mark `!` before the colon:

```text
<type>(<scope>)!: <subject>
```

### Examples:
- `feat(api)!: remove deprecated v1 authentication endpoints`
- `refactor(config)!: rename host to hostname in schema`

---

## 2. Multi-Line Footer Format (`BREAKING CHANGE:`)

A breaking commit MUST include a footer starting with `BREAKING CHANGE:` followed by a space and a clear explanation of what broke and how to migrate:

```text
<type>(<scope>)!: <subject>

[Optional body describing motivation and context]

BREAKING CHANGE: <detailed description of the breaking change and upgrade path>
```

### Complete Example:
```text
feat(auth)!: replace session cookies with jwt bearer tokens

Session-based authentication has been deprecated in favor of stateless JWT tokens
to support multi-region clustering.

BREAKING CHANGE: The /login endpoint no longer sets a Set-Cookie header. Clients
must now extract the `token` from the JSON response and pass it as
`Authorization: Bearer <token>` in subsequent requests.
```

---

## 3. The 50-Character Header Rule in Breaking Changes
Even with `!`, the first line MUST still obey the **<= 50 characters hard ceiling**.
- `feat(auth)!: switch to jwt bearer tokens` (41 chars) -> **Compliant**
- `feat(auth)!: completely remove all existing cookie auth mechanisms` (62 chars) -> **Violation! Compress it.**
