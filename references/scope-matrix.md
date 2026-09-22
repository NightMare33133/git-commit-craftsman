# Scope Matrix & Extraction Heuristics

The scope names the specific module, feature area, or architectural boundary affected by the commit.

---

## 1. Extraction Heuristics (How to pick a scope)

Follow this decision tree when analyzing the staged diff:

1. **Monorepo / Workspace**:
   - If the file is in `packages/core/...` -> scope is `(core)`.
   - If the file is in `apps/web/...` -> scope is `(web)`.
2. **Directory Name**:
   - If the file is in `src/auth/token_manager.py` -> scope is `(auth)`.
   - If the file is in `src/billing/tax.py` -> scope is `(billing)`.
3. **Component Name**:
   - If the file is `components/Navbar.vue` -> scope is `(navbar)`.
   - If the file is `services/order_service.go` -> scope is `(order)`.
4. **Tooling & Meta**:
   - If the file is `.github/workflows/ci.yml` -> scope is `(ci)`.
   - If the file is `package.json` or `requirements.txt` -> scope is `(deps)`.
   - If the file is `README.md` -> scope is `(readme)`.

---

## 2. Prohibited Generic Scopes

Never use the following generic or lazy scopes:
- ❌ `(misc)`
- ❌ `(all)`
- ❌ `(core)` (unless `core` is an actual directory or package name)
- ❌ `(fix)`
- ❌ `(code)`
- ❌ `(patch)`

If changes span multiple legitimate scopes, **re-verify atomicity**: you likely have a non-atomic diff that must be split!
