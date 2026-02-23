# CHANGELOG GUIDE

This guide explains how to use and maintain the `CHANGELOG.md` for the **Bank-With-High-Functionalities** project. Keeping a changelog consistent helps developers, contributors, and users understand the evolution of this project.  

---

## 1. Purpose of CHANGELOG.md

The `CHANGELOG.md` tracks all notable changes in the project, including:

- New features
- Bug fixes
- Documentation updates
- Refactoring
- Performance improvements
- Deprecated or removed functionality

A clear changelog improves transparency and makes releases easier to track.

---

## 2. Format

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html):

- Versions: `MAJOR.MINOR.PATCH`  
  - **MAJOR**: Breaking changes  
  - **MINOR**: New features, backward-compatible  
  - **PATCH**: Bug fixes, backward-compatible  

- Sections in each release:

  - `Added` → New features  
  - `Changed` → Changes in existing functionality  
  - `Deprecated` → Soon-to-be removed features  
  - `Removed` → Removed features  
  - `Fixed` → Bug fixes  
  - `Security` → Security fixes  

---

## 3. `[Unreleased]` Section

The `[Unreleased]` section is **temporary**. It contains all changes merged into the main branch but **not yet released as a version**.

### What to write here

- Any PR or commit that changes functionality  
- New features or modules  
- Bug fixes or performance improvements  
- Documentation updates  
- Breaking changes (mark clearly in `Changed`)

**Example:**

```md
## [Unreleased]

### Added
- Multi-account management support
- Transaction filtering by date and type

### Fixed
- Corrected bug where withdrawal exceeded balance
```

### When to clear `[Unreleased]`

When a release is tagged (e.g., `v1.0.0`), move all entries from `[Unreleased]` to the new version:

```md
## [1.0.0] - 2026-02-24

### Added
- Multi-account management support
- Transaction filtering by date and type

### Fixed
- Corrected bug where withdrawal exceeded balance
```

Then `[Unreleased]` becomes empty again for the next development cycle.

---

## 4. When and What to Write

Write or update the changelog **whenever a PR or commit merges into the `main` branch**:

| Type of Change  | Section to Write |                Notes                |
|-----------------|------------------|-------------------------------------|
| New feature     | `Added`          | Mention the feature/module clearly  |
| Bug fix         | `Fixed`          | Include affected functionality      |
| Breaking change | `Changed`        | Explain how it affects usage        |
| Deprecation     | `Deprecated`     | Indicate planned removal            |
| Removed feature | `Removed`        | Specify removed functionality       |
| Documentation   | `Changed`        | Only for relevant docs changes      |
| Security fix    | `Security`       | Must be precise about vulnerability |

**Tips:**

- Keep entries short but descriptive  
- Reference issue numbers or PRs if possible (`#23`)  

---

## 5. Boilerplate Template

Here’s a ready-to-use changelog structure:

```md
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
-

### Changed
-

### Deprecated
-

### Removed
-

### Fixed
-

### Security
-

---

## [1.0.0] - YYYY-MM-DD

### Added
-

### Changed
-

### Deprecated
-

### Removed
-

### Fixed
-

### Security
-
```

---

## 6. Commit Message Guidelines for CHANGELOG

When committing changes that affect the changelog, follow a consistent format. This helps maintain clarity and traceability.

### Format

```text
changelog: [section] - short description of change
```

Where:

- `changelog:` → prefix indicating this commit affects the changelog  
- `[section]` → one of `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`  
- `short description` → concise explanation of the change  

### Examples

**Adding a feature**
```text
changelog: [Added] - account management support
```

**Fixing a bug**
```text
changelog: [Fixed] - withdrawal calculation error when balance insufficient
```

**Documentation change**
```text
changelog: [Changed] - updated getting-started guide for setup clarity
```

**Security fix**
```text
changelog: [Security] - sanitize user input in transfer module
```

**Preparing for release**
```text
changelog: [Unreleased] - prepare entries for v1.0.0
```

### Best Practices

1. **Use present tense** → “Add feature”, not “Added feature”  
2. **Keep it short** → ~50 characters for the main line  
3. **Reference issues/PRs** if relevant → e.g., `[Fixed] login bug (#23)`  
4. **One commit per changelog entry** → keeps `[Unreleased]` neat  
5. **Separate commits** for multiple unrelated changes → improves clarity  

---

## 7. Maintaining the Changelog

- **Always update `[Unreleased]` first** for any new merged changes  
- **Move `[Unreleased]` to a new version** only when releasing  
- Keep history intact — do **not delete old releases**  
- Review changelog entries during PR review to ensure clarity  

---

## 8. Example Full Changelog Entry

```md
## [Unreleased]

### Added
- Account dashboard with live balance overview
- Transaction search and export feature

### Fixed
- Correct calculation of interest on fixed deposits
- Minor UI glitch on mobile login screen

### Security
- Sanitize user input in transfer module
```

---

> [!TIP]
> Treat `CHANGELOG.md` as a **living document**. Even small changes should be recorded to provide context for future contributors and maintainers.

--- 

This guide ensures everyone working on **Bank-With-High-Functionalities** follows the same process for documenting project history clearly, consistently, and with proper commit message conventions.
