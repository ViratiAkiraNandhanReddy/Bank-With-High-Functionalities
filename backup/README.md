
# 🗂️ Backup Directory

The `backup/` directory contains automated database snapshots used by the application to ensure data safety and recovery.  
These backups are created and managed internally by the application — **do not modify this folder unless you fully understand the implications.**

---

## 📁 Structure

```
backup/  
    ├── 01/  
    ├── 02/  
    └── 03/  
```

Each subdirectory (`01`, `02`, `03`) represents a full copy of the `database/` directory captured at a specific point in time.

---

## 🔄 Purpose

Backups are created automatically when:

- The application is **deleted/uninstalled**
- A **critical reset** or destructive operation occurs
- The system detects scenarios requiring data preservation

These backups allow the application to restore user data safely when needed.

---

## ♻️ Restoration

Backups are restored **only through the application interface**.

The UI allows you to:

- Restore any available backup (`01`, `02`, or `03`)
- Delete an existing backup
- Create a new backup snapshot

> ⚠️ Manual restoration by copying files is not recommended and may corrupt the system state.

---

## ➕ Creating New Backups

The system maintains a **maximum of three backups**.

If all three (`01`, `02`, `03`) already exist and a new database is created (fresh start):

1. The backup with the **least active users** is selected.
2. That backup is moved to the `bin/` directory (soft-deleted).
3. The new database snapshot replaces its slot.

This ensures the most relevant backups are retained automatically.

---

## 🗑️ Soft Deletion & Retention

When a backup is replaced:

- It is moved to: `bin/`
- It can still be restored **manually** within **30 days**
- After 30 days, it is **permanently deleted**

This acts as a safety net against accidental loss.

---

## ⚠️ Important Warning

🚫 Do **not** modify, rename, or delete backup folders manually unless you know exactly what you are doing.

Incorrect changes may cause:

- Data corruption
- Failed restorations
- Application errors
- Permanent data loss

Always use the application interface for backup management.

---

## ✅ Summary

- Contains up to **3 database backups**
- Managed automatically by the application
- Restorable via UI
- Old backups moved to `bin/` then deleted after 30 days
- Critical for data recovery

---

**In short:**  
This directory protects user data. Treat it as system-managed and read-only.
