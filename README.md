<div align="center">

<img src="assets/README/root-banner.jpg" width="100%" alt="Bank With High Functionalities">

# Bank With High Functionalities

**A Windows desktop banking application built with Python and CustomTkinter.**

[![Python](https://img.shields.io/badge/Python-3.15-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Documentation](https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/)
· [Issues](https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/issues)
· [Discussions](https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/discussions)

</div>

## Overview

Bank With High Functionalities is a modular desktop banking application for Windows. It provides a graphical sign-in and sign-up experience, a user dashboard for account and transaction activity, an administrator area, email-based account workflows, and a configurable persistence layer.

The application is designed around a shared server abstraction. The interface does not need to know whether data is stored in JSON files, SQLite, or MySQL; the selected backend exposes the same authentication, lookup, management, and schema services.

> **Simulation only:** This project is a banking simulation for learning and development. It does not contain, process, transfer, or represent real money, real bank accounts, or real financial transactions. It is not a production banking platform, financial service, or substitute for a regulated banking system.

## Features

### Authentication and accounts

- User sign-in and account registration
- Password confirmation and minimum password-length validation
- Administrator authentication flow
- Backup-code support for account recovery
- Login, failed-login, and logout security events
- Last-login tracking
- Optional email address on user accounts
- Product activation flow on first launch

### Banking dashboard

- Account information and current balance
- Deposit and withdrawal actions
- User-to-user transfers
- Transaction history with transaction type, amount, counterparty, and timestamp
- Frequently used transfer recipients
- Application announcements
- Recent security activity
- Full transaction and security-history overlays
- Settings and support overlays
- Local-time display for transaction and security timestamps

### Administrator area

- Administrator navigation and status information
- User and access management
- Application overview and settings views
- Activity and history views
- Issues, announcements, and broadcast views

### Email workflows

- Account welcome emails
- Email verification
- Password-recovery OTP flow
- HTML email templates
- Gmail SMTP integration over SSL

### Storage backends

- JSON file storage for simple local development
- SQLite storage for the default local desktop setup
- MySQL storage for shared or server-backed deployments
- Common contracts across all backends
- Automatic schema initialization for supported storage modes

## Requirements

### Supported environment

- Windows
- Python 3.15
- A working graphical desktop session
- Internet access only when using email delivery, external links, or network-dependent features

The application uses Windows-specific helpers, including Win32 calls, `hPyT`, and `pywinstyles`. Other operating systems are not currently supported.

### Runtime dependencies

The runtime dependencies are listed in [`requirements.txt`](requirements.txt):

| Package | Purpose |
| --- | --- |
| `customtkinter` | Desktop user interface |
| `Pillow` | Image and asset handling |
| `hPyT` | Windows title-bar and window helpers |
| `pywinstyles` | Windows window styling |
| `python-dotenv` | Environment-variable loading |
| `caesarcipher-extended` | Existing application encryption utilities |
| `mysql-connector-python` | MySQL backend connectivity |

Development tooling is listed separately in [`etc/requirements-dev.txt`](etc/requirements-dev.txt).

## Installation

Open PowerShell in the repository directory and create a virtual environment:

```powershell
git clone https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities.git
cd Bank-With-High-Functionalities

py -3.15 -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell prevents script activation, run the application with the virtual-environment interpreter directly:

```powershell
.\.venv\Scripts\python.exe main.py
```

To install development tooling:

```powershell
python -m pip install -r etc\requirements-dev.txt
```

## Configuration

### Database selection

The selected backend is controlled by [`database/config.json`](database/config.json):

```json
{
    "is_activated": false,
    "DATABASE TYPE": "SQLite3"
}
```

Supported values for `DATABASE TYPE` are:

| Value | Backend | Data location |
| --- | --- | --- |
| `SQLite3` | Local SQLite database | `database/sqlite3/database.sqlite3` |
| `JSON` | Local JSON files | `database/json/database.json` |
| `MySQL` | MySQL server | Configured through `.env` |

SQLite is the recommended backend for local development. Change the value before starting the application and restart the program after changing it.

The application may update runtime fields in `database/config.json`, including activation state and the most recent launch time. Treat this file as runtime configuration rather than immutable source code.

### Environment variables

Copy the example file to `.env`:

```powershell
Copy-Item .env.example .env
```

Never commit `.env`. Use `.env.example` as the variable-name reference.

#### MySQL configuration

Set these variables when `DATABASE TYPE` is `MySQL`:

```dotenv
MYSQL__DB_USERNAME=
MYSQL__DB_PASSWORD=
MYSQL__DB_HOSTNAME=127.0.0.1
MYSQL__DB_PORTNMBR=3306
MYSQL__DB_CHAR_SET=utf8mb4
MYSQL__DB_DATABASE=bank_with_high_functionalities
```

Create the database named by `MYSQL__DB_DATABASE` before launching the application. The backend creates its tables when its schema services are initialized. Use a dedicated database account with only the permissions required by the deployment.

#### Gmail SMTP configuration

Email workflows use Gmail SMTP. Configure an app password rather than a normal account password:

```dotenv
SMTP__MAIL_ADDRESS=your-address@example.com
SMTP__APP_PASSWORD=your-gmail-app-password
```

Email functionality is optional for local work, but verification, welcome messages, and password recovery require valid SMTP settings.

### Product activation

On the first launch, the application opens its product-activation flow when `is_activated` is false. Complete that flow with a valid project activation key, then launch the sign-in screen. Do not publish activation keys, SMTP credentials, database passwords, or generated runtime data.

## Running the application

From the repository root:

```powershell
python main.py
```

Or, without activating the virtual environment:

```powershell
.\.venv\Scripts\python.exe main.py
```

The startup sequence is:

1. Load shared configuration and environment variables.
2. Select the backend from `database/config.json`.
3. Run product activation if the application is not activated.
4. Record the launch timestamp in the runtime configuration.
5. Open the sign-in interface.

For a clean local SQLite setup, remove or rename only the specific local database file while the application is stopped, then start the application again. Do not delete the repository or broad database directories.

## Project structure

```text
.
├── main.py                         # Application entry point
├── requirements.txt                # Runtime dependencies
├── etc/
│   └── requirements-dev.txt        # Development dependencies
├── database/
│   ├── config.json                 # Backend selection and runtime state
│   ├── json/                       # JSON backend data
│   ├── schema/                     # Database documentation
│   └── sqlite3/                    # SQLite database files
├── src/
│   ├── __init__.py                 # Shared imports and application setup
│   ├── __etc__/                    # Supporting flows, including activation
│   ├── __mail__/                   # Email services and HTML templates
│   ├── __server__/                 # Backend selection and persistence APIs
│   │   ├── __base__/               # Shared backend contracts
│   │   ├── _json/                  # JSON implementation
│   │   ├── _mysql/                 # MySQL implementation
│   │   └── _sqlite3/               # SQLite implementation
│   ├── administrator/              # Administrator interface
│   ├── dashboard/                  # User dashboard, tiles, and overlays
│   ├── sign_in/                    # Sign-in flow
│   ├── sign_up/                    # Account-registration flow
│   ├── assets/                     # Application asset helpers
│   └── utils/                      # Browser, theme, network, and privacy helpers
├── assets/                         # Shared images, icons, and branding
├── docs/                           # Generated/static project documentation
├── tests/                          # Test package and future automated tests
├── ARCHITECTURE.md                 # Architecture reference
├── SECURITY.md                     # Vulnerability-reporting policy
├── SUPPORT.md                      # Support and issue-reporting guidance
├── CODE_OF_CONDUCT.md              # Community standards
└── LICENSE                         # MIT license
```

## Architecture

The application exposes a single `SERVER` namespace from `src.__server__`. The namespace is selected from the configured backend:

```python
SERVER.authentication.user
SERVER.authentication.admin
SERVER.lookup.user
SERVER.lookup.admin
SERVER.lookup.application
SERVER.lookup.security_event
SERVER.management.user
SERVER.management.admin
SERVER.management.application
SERVER.management.security_event
SERVER.schema.user
SERVER.schema.admin
SERVER.schema.transaction
SERVER.schema.announcement
SERVER.schema.security_event
```

UI code should use these services rather than opening database connections or selecting a backend directly. When changing persistence behavior, update the shared contract in `src/__server__/__base__/` and keep the JSON, SQLite, and MySQL implementations consistent.

The core data areas are:

- `USERS` — user accounts and balances
- `ADMINS` — administrator accounts
- `TRANSACTIONS` — deposits, withdrawals, and transfers
- `ANNOUNCEMENT` — the current application announcement
- `SECURITY_EVENTS` — login and account-security activity

Database records use uppercase field names such as `UUID`, `USERNAME`, `BALANCE`, and `CREATED_AT`.

More detail is available in [`architecture.md`](architecture.md), [`database/json/README.md`](database/json/README.md), and the source contracts.

## Development

### Formatting

The repository uses Black for formatting. Check formatting without changing files:

```powershell
black --check .
```

Apply formatting locally when needed:

```powershell
black .
```

The repository also contains a contributor-list workflow:

```powershell
node .github/scripts/lint-contributors.js
```

### Testing

There is currently no committed application test suite beyond the `tests` package. If a targeted local test is available, run it with:

```powershell
python -m pytest tests\test_file.py::test_name
```

For changes affecting a backend, verify the corresponding JSON, SQLite, and MySQL contracts where practical. Avoid using a real account, production credentials, or shared financial data during development.

### Code conventions

- Preserve the repository's Python 3.15 lazy-import syntax.
- Keep persistence-specific SQL, JSON access, and connections inside the selected backend package.
- Keep public method signatures and return shapes aligned with `src/__server__/__base__/`.
- Reuse `SERVER` services and existing CustomTkinter asset helpers.
- Use four-space indentation and keep a final newline in text files.

## Data and safety notes

This project simulates account and financial data in local development files. It does not contain or process real money. All balances, deposits, withdrawals, transfers, and transactions are simulated values for demonstration and development only.

Before experimenting:

- Back up any local database you care about.
- Do not commit `.env`, database passwords, SMTP app passwords, or personal data.
- Do not use real banking credentials or real customer information.
- Restrict access to SQLite, JSON, and MySQL configuration files.
- Use a dedicated MySQL database and least-privilege account.
- Treat the application as a development project, not a regulated financial system.

The database files under `database/` may be generated or modified at runtime and should not be treated as portable production data.

## Documentation and project links

- [Project documentation](https://viratiakiranandhanreddy.github.io/Bank-With-High-Functionalities/)
- [Architecture](ARCHITECTURE.md)
- [Changelog](CHANGELOG.md)
- [Security policy](SECURITY.md)
- [Support guide](SUPPORT.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Contributors](CONTRIBUTORS.md)
- [License](LICENSE)

## Contributing

Contributions are welcome when they preserve the existing architecture and documentation standards. Before opening a pull request:

1. Read the architecture and relevant backend contracts.
2. Keep changes focused and avoid committing runtime data or secrets.
3. Run the smallest relevant formatting, lint, and validation commands.
4. Update documentation and the changelog when behavior changes.
5. Explain backend, schema, configuration, or security implications in the pull request.

Please use GitHub Issues for reproducible defects and feature proposals, and follow [`SECURITY.md`](SECURITY.md) for vulnerabilities. Community participation is governed by [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

## License

Bank With High Functionalities is distributed under the [MIT License](LICENSE).
