# Executable Source

This directory contains the source code for standalone executable files that are distributed at the repository root.

The compiled executables in the root directory are built from the sources maintained here. Keeping the sources separate ensures clarity between human-readable implementation and generated binary artifacts.

## Scope

This directory is intended only for executables that:

- Are placed directly in the repository root after build
- Do not belong to a dedicated component with its own `source/` and `dist/` structure
- Represent small or single-purpose utilities bundled with the project

## Exclusions

Executables that are part of larger components — such as Installer, Uninstaller, or other packaged tools — are organized in their own directories with independent `source/` and `dist/` layouts. Their sources are **not** located here.

## Build Relationship

- **Source of truth:** `exe-source/`
- **Built artifacts:** repository root (`/`)
- **Other components:** their respective `<component>/source` » `<component>/dist`

The root-level executables should always be reproducible from the sources in this directory.

## Notes

- Do not edit compiled executables directly.
- Update or modify behavior only through the corresponding source files here.
- If an executable grows into a full component (e.g., requires packaging, assets, or installer logic), it should be migrated to its own dedicated directory structure.
