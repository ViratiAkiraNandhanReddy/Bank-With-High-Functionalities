# Architecture

**Last updated:** 25 October 2026

## System overview

Bank With High Functionalities is a Windows-oriented Python desktop application
implemented with CustomTkinter. It is a **simulation only**: balances,
deposits, withdrawals, transfers, and transaction records are fictional
development data. The application does not contain, process, or represent real
money or real bank accounts.

The system is organized into four primary layers:

1. **Presentation** — CustomTkinter windows, screens, dashboard tiles,
   overlays, and administrator views.
2. **Application services** — Authentication flows, activation, email
   workflows, validation, and shared utilities.
3. **Persistence abstraction** — The `SERVER` namespace and its authentication,
   lookup, management, and schema services.
4. **Storage implementations** — JSON files, SQLite, or MySQL selected at
   runtime.

The presentation layer communicates with persistence through the shared
`SERVER` interface. UI modules must not select a database, construct SQL, or
open backend connections directly.

## Runtime entry point

`main.py` is the application entry point:

1. Imports shared configuration and the sign-in interface.
2. Checks whether product activation has been completed.
3. Opens the activation flow when `is_activated` is false.
4. Records the current launch time in the runtime configuration object.
5. Starts `sign_in_interface().sign_in()`.

The shared `src/__init__.py` module loads `.env`, exposes project links and
common dependencies, imports the selected server, and provides Windows window
helpers. The application uses native Win32 calls, `hPyT`, and `pywinstyles`
for borderless windows, title-bar behavior, opacity, and window styling.

## Repository structure

| Path | Responsibility |
| --- | --- |
| `main.py` | Startup, activation check, and sign-in launch. |
| `src/__init__.py` | Shared imports, configuration, environment loading, project links, and Windows helpers. |
| `src/sign_in/` | User and administrator sign-in UI and session entry flow. |
| `src/sign_up/` | New user registration UI and validation. |
| `src/dashboard/` | User dashboard, tiles, financial-simulation actions, and overlays. |
| `src/administrator/` | Administrator navigation, status panel, and management views. |
| `src/__server__/` | Backend selection, contracts, connections, schemas, and storage implementations. |
| `src/__mail__/` | SMTP email services and HTML templates. |
| `src/__etc__/` | Supporting flows such as product activation. |
| `src/utils/` | Browser, greeting, networking, privacy, and theme helpers. |
| `src/assets/` | Python asset loaders and application branding helpers. |
| `assets/` | Images, icons, banners, and logos. |
| `database/` | Runtime configuration and local persistence data. |
| `docs/` | Static project documentation. |
| `tests/` | Test package and future automated tests. |

## UI and application flow

### Sign-in and registration

The sign-in interface is the entry point for users and administrators. The
registration interface validates required fields, password length, and password
confirmation before calling:

```python
SERVER.management.user.create(username, password, full_name, email)
```

Authentication accepts the shared user or administrator service. User
authentication supports password, backup-code, and email-address operations.
Successful and failed authentication events are recorded through the security
event management service where applicable.

### User dashboard

After user authentication, `dashboard_interface` creates a dashboard composed
of reusable components:

- Account information and current balance
- Deposit, withdrawal, and transfer actions
- Announcements
- Security activity
- Recent transactions
- Frequently used transfer recipients
- Transaction, security, support, and settings overlays

The dashboard resolves data through `SERVER.lookup` and changes state through
`SERVER.management`. It updates last-login information and records logout
activity when the user exits the dashboard.

### Administrator interface

The administrator interface is a separate view with navigation and a status
panel. Its views cover:

- Overview and application status
- Users and access
- Activity and history
- Issues and broadcasts
- Settings

Administrator functionality uses administrator lookup and management services
instead of accessing storage directly.

## Persistence architecture

### Backend selection

`src/__server__/__init__.py` reads `DATABASE TYPE` from
`database/config.json` and binds the matching implementation to `SERVER`:

| Configuration value | Implementation | Storage |
| --- | --- | --- |
| `JSON` | `src/__server__/_json/` | `database/json/database.json` |
| `SQLite3` | `src/__server__/_sqlite3/` | `database/sqlite3/database.sqlite3` |
| `MySQL` | `src/__server__/_mysql/` | Configured MySQL database |

The value must match one of the supported names. SQLite is the default local
development backend because it requires no separate server.

### Shared backend contracts

The abstract classes in `src/__server__/__base__/` define the public behavior
that every backend must provide:

```text
authentication
├── user
└── admin

lookup
├── user
├── admin
├── application
└── security_event

management
├── user
├── admin
├── application
└── security_event

schema
├── user
├── admin
├── transaction
├── announcement
└── security_event
```

The contracts are class-based namespaces and their methods are generally class
methods. Backend implementations should preserve method signatures, accepted
identifiers, return values, and tuple shapes.

### Authentication services

User authentication supports:

- Password verification by username or UUID
- Backup-code verification by username or UUID
- Email-address verification by username or UUID
- Last-login updates

Administrator authentication supports password, backup-code, and email-address
verification by administrator username.

Passwords and backup codes are handled by the existing application encryption
and identifier utilities. Changes to credential behavior must be made
consistently across all backends.

### Lookup services

User lookup exposes account existence, UUID resolution, balance, full name,
last login, creation time, email, backup code, recent transactions, and
frequent transfer recipients.

Administrator lookup exposes user summaries, administrator summaries, and
recent security events. Application lookup returns the current announcement,
while security-event lookup returns recent events for a user.

### Management services

User management exposes:

- Account creation
- Deposits
- Withdrawals
- User-to-user transfers
- Password changes
- Username changes
- Account deletion

Administrator management exposes administrator creation and password changes.
Application management updates the current announcement. Security-event
management records events such as login, failed login, and logout.

Financial operations are simulated state changes. They update fictional
balances and transaction records and must not be described as real payments or
banking operations.

## Data model

The storage backends represent the following logical tables or collections:

| Entity | Purpose | Important fields |
| --- | --- | --- |
| `USERS` | Simulated customer accounts | `UUID`, `USERNAME`, `PASSWORD`, `EMAIL`, `BACKUP_CODE`, `LAST_LOGIN`, `FULL_NAME`, `BALANCE`, `CREATED_AT` |
| `ADMINS` | Administrator accounts | `USERNAME`, `PASSWORD`, `EMAIL`, `BACKUP_CODE`, `CREATED_AT` |
| `TRANSACTIONS` | Simulated financial activity | `TRANSACTION_ID`, `USER_UUID`, `COUNTERPARTY_USERNAME`, `AMOUNT`, `TRANSACTION_TYPE`, `TIMESTAMP` |
| `ANNOUNCEMENT` | Current application-wide message | `ANNOUNCEMENT_ID`, `CONTENT`, `UPDATED_AT` |
| `SECURITY_EVENTS` | Account-security activity | `EVENT_ID`, `USER_UUID`, `EVENT_TYPE`, `CREATED_AT` |

Field names are uppercase across JSON and SQL implementations. UUIDs identify
users internally, while several public service methods accept either a
username or UUID and resolve the identifier inside the backend.

Transactions reference the owning user's UUID. SQL implementations use foreign
keys with cascade behavior for dependent transaction and security-event rows.
The announcement collection/table is intentionally limited to one current
announcement with ID `1`.

## Backend implementation details

### SQLite

The SQLite backend opens `database/sqlite3/database.sqlite3` and enables
foreign-key enforcement through `PRAGMA foreign_keys = ON`. Schema classes
create tables if they do not exist and seed the default administrator and
announcement records where required.

SQLite is the recommended backend for local development and demonstrations.
The database file is runtime state and may change when the application starts
or when simulated account activity occurs.

### JSON

The JSON backend loads `database/json/database.json` into an in-memory
dictionary whose keys are table names and whose values are lists of records.
Missing tables are created on demand. Writes use a temporary file followed by a
replacement operation to reduce the chance of leaving a partially written
database file.

Do not edit the JSON database while the application is running. The JSON
backend is appropriate for simple local experiments, not concurrent multi-user
deployment.

### MySQL

The MySQL backend uses `mysql-connector-python`. Connection details are loaded
from environment variables, including host, port, character set, database,
username, and password. Its schema uses InnoDB tables and SQL foreign keys.

MySQL is intended for server-backed development scenarios. It requires a
pre-created database and a dedicated account with appropriate privileges.
Credentials must remain in `.env` or another protected environment mechanism.

## Email architecture

`src/__mail__/` contains separate flows for:

- Email verification
- Password recovery
- Welcome messages

HTML templates are stored in `src/__mail__/templates/`. The email layer builds
messages with `email.message.EmailMessage` and sends them through Gmail SMTP
over SSL. It reads:

```dotenv
SMTP__MAIL_ADDRESS=
SMTP__APP_PASSWORD=
```

The password-recovery flow generates a temporary one-time code and presents a
countdown-based verification experience. Email delivery is optional for
offline UI development but required for email verification, welcome messages,
and password recovery.

## Configuration and runtime state

`database/config.json` contains runtime settings such as:

```json
{
    "is_activated": true,
    "Recently Used On": "...",
    "DATABASE TYPE": "SQLite3"
}
```

The activation state and selected backend are read during startup. The launch
timestamp is updated by the application at runtime. Generated databases and
runtime configuration should be treated as environment state, not as stable
source definitions.

`.env.example` documents the names required for MySQL and SMTP configuration.
The real `.env` file is local secret material and must not be committed.

## Dependency and platform boundaries

The application depends on:

- Python 3.15
- CustomTkinter for the desktop UI
- Pillow for image handling
- `hPyT` and `pywinstyles` for Windows window behavior
- `python-dotenv` for environment loading
- `caesarcipher-extended` for existing encryption utilities
- `mysql-connector-python` for MySQL connectivity

Win32 APIs and Windows-specific UI libraries are architectural dependencies,
not optional enhancements. Cross-platform support would require a separate
window-management and styling abstraction.

## Extension guidelines

When adding a feature:

1. Define or update the shared contract in `src/__server__/__base__/` when
   persistence behavior is involved.
2. Implement the behavior in `_json`, `_sqlite3`, and `_mysql` as applicable.
3. Keep SQL, JSON serialization, and connection handling inside the backend.
4. Expose the behavior to UI code through `SERVER`.
5. Reuse existing dashboard, administrator, asset, and utility patterns.
6. Update the data model and documentation when adding fields or entities.
7. Preserve the simulation-only boundary in user-facing text and workflows.

Changes to schemas, identifiers, transaction semantics, authentication, or
return shapes can affect every backend and all dependent UI components.

## Development checks

Use the repository's existing checks from the project root:

```powershell
black --check .
node .github/scripts/lint-contributors.js
```

There is currently no committed application test suite beyond the `tests`
package. Backend changes should be verified against the relevant storage
implementation and, where practical, the corresponding shared contracts and
other backend implementations.

## Related documentation

- [`README.md`](README.md) — installation, usage, and project overview
- [`database/json/README.md`](database/json/README.md) — JSON storage details
- [`CHANGELOG.md`](CHANGELOG.md) — release history and known limitations
- [`SECURITY.md`](SECURITY.md) — vulnerability reporting policy
- [`SUPPORT.md`](SUPPORT.md) — support and issue-reporting guidance
