# Bin Directory

The `bin/` directory serves as a temporary holding area for data that has been **deleted by the application** but is still within the retention window for possible recovery.

It functions similarly to a recycle bin or trash system for application-managed data.

---

## 📁 Purpose

When the application deletes data (such as backups or other managed resources), the data is **not immediately removed permanently**.  
Instead, it is moved to the `bin/` directory to allow a limited-time recovery window.

This provides protection against:

- Accidental deletion
- Backup rotation replacement
- User reset operations
- System cleanup tasks

---

## ⏳ Retention Policy

All items inside `bin/` follow a strict lifecycle:

1. Data is moved to `bin/` when deleted by the application
2. It remains recoverable for **30 days**
3. After 30 days, it is **permanently deleted** by the application

After permanent deletion, recovery is no longer possible.

---

## ♻️ Restoration

Some items in `bin/` may be restored manually if needed (for example, replaced backups).

Restoration is typically done by:

- Moving the item back to its original directory
- Using the application interface (if supported)

> [!WARNING]
> Not all bin items are guaranteed to be restorable depending on context.

---

## 🔄 Relation to Backups

When the system needs to create a new backup but all backup slots are occupied:

- The least-active backup is moved from `backup/` → `bin/`
- It remains recoverable for 30 days
- Then permanently deleted

This ensures backup rotation without immediate data loss.

---

## ⚠️ Important Warning

🚫 Do **not** modify or delete files inside `bin/` unless you understand the consequences.

Improper changes may cause:

- Broken restore operations
- Inconsistent backup state
- Application errors
- Permanent data loss

The application manages this directory automatically.

---

## ✅ Summary

- Temporary storage for deleted application data
- Acts like a recycle bin
- 30-day recovery window
- Automatically purged after retention period
- Managed by application logic

---

**In short:**  
`bin/` contains recently deleted data awaiting permanent removal.  
Treat it as system-managed and avoid manual intervention.
