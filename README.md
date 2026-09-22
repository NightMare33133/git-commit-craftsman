# 🛠️ Git Commit Craftsman (Git 原子提交与规约专家)

<p align="center">
  <b>面向企业级研发协同与大模型 Agent 的 Git 提交规约智能体技能</b><br>
  <i>严守原子提交（Atomic Commit）底线，粉碎大模型偷懒借口，让每一次提交都成为团队的沟通资产。</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Agent%20Skill-Antigravity%20%7C%20Claude%20%7C%20Dify-blue" alt="Skill Standard">
  <img src="https://img.shields.io/badge/Standard-Conventional%20Commits-green" alt="Conventional Commits">
  <img src="https://img.shields.io/badge/License-MIT-purple" alt="License">
</p>

---

## 🎯 为什么需要这个 Skill？

在日常团队协作中，`git log` 是代码库的“飞机黑匣子”。然而大多数开发者和大模型经常写出以下**四大垃圾提交灾难**：

1. **敷衍废话型**：满屏的 `update`, `fix bug`, `modify`, `test`，出线上事故排查时根本不知道改了什么；
2. **“大杂烩 / 巨石型”（破坏原子性）**：改了前端样式，顺便修了数据库 Bug，还升级了依赖，揉成一条提交。导致后续想 `git revert` 撤销样式时，连带把核心修复也一并抹除！
3. **情绪发泄型**：`"终于改好了"`, `"草怎么还是不行"`，破坏开源与企业交付形象；
4. **散文小作文型**：大模型生成一段 60 词的长篇论文，彻底挤爆终端 `git log --oneline`。

**`git-commit-craftsman` 的使命，就是将大模型从一个“谄媚顺从的文本生成器”，驯化为一个“严守发布工程规约的资深 Release 工程师”！**

---

## 🌟 核心特性

- ⚡ **原子性前置拦截（Atomicity Gate）**：
  在生成任何 commit 前，优先审查 `git diff` 是否跨越多个业务领域。一旦检测到跨域混杂，**严正拒绝单次提交**，强制拆解为多步原子提交方案。
- 📏 **Conventional Commits 铁律**：
  严格遵循 `<type>(<scope>): <subject>` 结构，锁死 8 大标准类型，必须包含具象的作用域（Scope）。
- 🚫 **50 字符硬天花板**：
  Header 行严格禁止超过 50 字符，51 字符即判定为不合格，强制使用紧凑动词。
- 💥 **借口粉碎机（Excuse Crusher）**：
  预置认知防御表，当场定点扼杀大模型常见的自欺欺人借口（*“改动很小我就合并了”*、*“用户要一条我就给一条”* 等）。
- 🎯 **纯正祈使现在时**：
  只使用 `add`, `fix`, `prevent`，严禁 `fixed`, `adds`, `updating` 等过去式或进行时。
- 🤐 **零对话废话（Zero Fluff）**：
  只输出开箱即用的 Git 命令块与一行技术依据（Rationale），杜绝客套寒暄。

---

## 🗺️ 技能演进四部曲（Roadmap）

本项目采用真实软件工程的递进式演化：

- [x] **V1 雏形版（MVP）**：实现 SDO 意图双向路由、基础原子性检查与 Conventional Commits 格式化。
- [x] **V2 规约版（Iron Rules）**：引入《认知铁律 The Iron Law》、《借口粉碎表 Excuse Crusher》与发包前强制自检清单。
- [x] **V3 结构版（Onion Decoupling）**：将枚举字典、多语言规范抽离到 `references/` 目录，轻量化主指令上下文。
- [x] **V4 工业版（Physical Gate）**：引入 `scripts/` Python 正则门禁，通过 Exit Code 0/1 打造确定性物理阻断。

---

## 📦 安装与挂载方式

### 方式一：在 Google Antigravity 中全局挂载
克隆或复制本项目到全局配置目录即可生效：
```bash
git clone https://github.com/NightMare33133/git-commit-craftsman.git ~/.gemini/config/skills/git-commit-craftsman
```

### 方式二：在独立项目/工作区中挂载
将技能放到项目的 `.agents/skills/` 目录下：
```bash
mkdir -p .agents/skills
git clone https://github.com/NightMare33133/git-commit-craftsman.git .agents/skills/git-commit-craftsman
```

---

## 💬 触发与使用体验

在对话中直接使用日常语言即可自动激活技能：

* “帮我写个 commit”
* “提交这段代码”
* “write a commit message for staged changes”
* “prepare git commit”

### 示例 1：原子修复（标准通过）
```bash
git commit -m "fix(auth): refresh token 60s before expiration"
```
**Rationale**: Fixes premature session expiry by refreshing the access token within a safety window.

### 示例 2：混杂改动（拒绝并拆分）
> ⚠️ **Atomicity Alert**: Detected 2 distinct logical changes in this diff. Split into 2 atomic commits:
>
> ```bash
> # Step 1: UI copywriting change
> git add pages/home.vue
> git commit -m "style(home): update purchase button label"
>
> # Step 2: Core refund algorithm bugfix
> git add services/refund.py
> git commit -m "fix(refund): resolve precision issue in refund calculation"
> ```

---

## 🤖 自动化物理门禁 (Verification Gate)

本项目在 `scripts/` 目录内置了纯 Python 确定性门禁校验器，**0 Token 消耗，提供毫秒级 Exit Code 物理阻断**：

```bash
# 运行单元自测试套件（8 大核心规则全覆盖）
python3 scripts/verify_commit.py --self-test

# 校验一条提交信息
python3 scripts/verify_commit.py "feat(auth): add google oauth2 login"
# ✅ 输出：[GATE APPROVED] Commit message strictly satisfies all craftsman rules. (Exit 0)

python3 scripts/verify_commit.py "fix(auth): fixed token expiration bug in user authentication session"
# ❌ 输出：[GATE REJECTED] Commit message violated craftsman rules:
#    • Header exceeds 50-character ceiling: detected 67 characters (17 chars over limit).
#    • Subject verb must be bare imperative, not past/third-person. Found: 'fixed'.
# (Exit 1)
```

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 许可协议。
