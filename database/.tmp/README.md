# `.tmp/`

This folder is used as a dedicated **runtime temporary workspace** for the application. It stores files that are created dynamically during execution to support internal operations, intermediate processing, and short-lived data handling needs.

---

## Purpose

The `.tmp/` directory is used as a **working space for short-lived data**, such as:

- Cached runtime assets
- Temporary downloads
- Intermediate processing files
- Installer/session state data
- Extracted archives (before final placement)
- Logging buffers (if enabled temporarily)

These files are **not part of the final application state**.

---

## Lifecycle

Files inside `.tmp/` are:

1. Created during runtime
2. Used internally by the application
3. Deleted automatically after use (or on next startup)
4. Safe to remove manually if the application is not running

---

> [!CAUTION]
> Files may be deleted without warning by the application

---

## Cleanup Behavior

The application may:

- Clear `.tmp/` on startup
- Clear `.tmp/` on exit
- Periodically purge unused files
- Overwrite existing temporary data

---

## Safety

This directory is designed for **non-critical, disposable data only**.  
Any important data should be stored outside `.tmp/`.

---

## Summary

`.tmp/` is a **volatile runtime workspace** used to support internal application operations and improve performance, without affecting permanent storage.
