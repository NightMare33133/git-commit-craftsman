# Conventional Commits: Type & SemVer Dictionary

This dictionary defines the exact semantic meaning of each commit type and its impact on Semantic Versioning (SemVer: `MAJOR.MINOR.PATCH`).

---

## 1. Primary Types (Affects Versioning)

| Type | SemVer Impact | Meaning | Typical Use Cases |
| :--- | :--- | :--- | :--- |
| **`feat`** | **MINOR** (`x.Y.z`) | New user-facing feature or capability | Adding a new API endpoint, new UI component, new CLI command. |
| **`fix`** | **PATCH** (`x.y.Z`) | Bugfix that patches defect without API break | Fixing a calculation error, handling null pointer, resolving memory leak. |
| **`perf`** | **PATCH** (`x.y.Z`) | Performance improvement without changing behavior | Optimizing database index query, memoizing expensive function. |

---

## 2. Secondary Types (Zero Version Bump)

These types indicate changes that do not alter the production application logic directly:

| Type | Meaning | Permitted Scopes | Prohibited Usage |
| :--- | :--- | :--- | :--- |
| **`refactor`** | Code change that neither fixes a bug nor adds a feature | Module name, class name, logic unit | Never use if business logic, API inputs, or outputs changed. |
| **`docs`** | Documentation only changes | `readme`, `api-docs`, `comments` | Never use if any code implementation changed. |
| **`style`** | Code style / formatting changes that do not affect code meaning | `lint`, `prettier`, `whitespace` | Never use for CSS layout changes (use `style(ui)` or `feat(ui)`). |
| **`test`** | Adding missing tests or correcting existing tests | `unit`, `e2e`, `fixtures` | Never use for test runner framework upgrades (use `chore(deps)`). |
| **`chore`** | Build tasks, package updates, dev tooling | `deps`, `build`, `release`, `ci` | Never use for application source code. |

---

## 3. Disambiguation Guide: Common Confusions

### `refactor` vs `chore`
- **Use `refactor`** when modifying internal application structure (e.g. splitting a 500-line class into 3 classes).
- **Use `chore`** when modifying auxiliary tooling, tsconfig, build scripts, or updating dependencies.

### `fix` vs `refactor`
- If the previous code caused an error/bug that users could encounter -> **`fix`**.
- If the previous code worked correctly but was messy/slow -> **`refactor`** or **`perf`**.
