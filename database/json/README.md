# JSON database

Select the JSON backend by setting `"DATABASE TYPE": "JSON"` in
[`../config.json`](../config.json). The database is stored in
`database/json/database.json`, created when schema methods are initialized.

The file contains arrays named `USERS`, `ADMINS`, `TRANSACTIONS`,
`ANNOUNCEMENT`, and `SECURITY_EVENTS`. Records use the same uppercase field
names as the SQLite tables. User records require `UUID`, `USERNAME`,
`PASSWORD`, `BACKUP_CODE`, and `FULL_NAME`; optional fields include `EMAIL`,
`LAST_LOGIN`, `BALANCE`, and `CREATED_AT`. Do not edit the file while the
application is running.

The backend supports the same authentication, lookup, account-management,
transaction-history, announcement, and security-event operations as SQLite.