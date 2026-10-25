# Copilot instructions

## Project shape

This is a Windows-oriented Python 3.15 desktop banking application. The UI is built with CustomTkinter and uses Windows-specific helpers (`hPyT`, `pywinstyles`, and Win32 calls). The application starts at `main.py`, which handles product activation, records the launch time in `database/config.json`, and opens the sign-in flow.

The main application areas are:

- `src/sign_in/` and `src/sign_up/`: authentication and account-registration UI flows.
- `src/dashboard/`: user dashboard, overlays, tiles, and deposit/withdraw/transfer actions.
- `src/administrator/`: administrator navigation and views.
- `src/__mail__/`: SMTP email verification, password recovery, and welcome-email flows using HTML templates in `src/__mail__/templates/`.
- `src/__server__/`: persistence abstraction and backend implementations.
- `database/`: runtime configuration plus JSON and SQLite data.

## Build, run, test, and lint

There is no packaging/build script. Install runtime dependencies and launch the desktop application from the repository root:

```powershell
python -m pip install -r requirements.txt
python main.py
```

Development tooling is listed separately:

```powershell
python -m pip install -r etc/requirements-dev.txt
```

The CI formatting check runs Black against the whole repository:

```powershell
black --check .
```

To apply Black formatting locally:

```powershell
black .
```

The contributor-list workflow is a separate Node.js check:

```powershell
node .github/scripts/lint-contributors.js
```

There is currently no committed test suite beyond `tests/__init__.py`, and pytest is not declared in the project requirements. If a local pytest test is available, target it rather than running unrelated tests:

```powershell
python -m pytest tests\test_file.py::test_name
```

## Architecture and data flow

`src/__server__/__init__.py` reads `database/config.json` and exposes one backend as `SERVER` based on `"DATABASE TYPE"`:

| Configuration value | Backend |
| --- | --- |
| `JSON` | `src/__server__/_json/` |
| `SQLite3` | `src/__server__/_sqlite3/` |
| `MySQL` | `src/__server__/_mysql/` |

All backends implement the abstract contracts in `src/__server__/__base__/`. The public shape is intentionally uniform:

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

UI code should use these `SERVER` services and should not select a database or open backend connections directly. Changes to authentication, lookup, management, or schema behavior usually need corresponding updates in all three backend directories and their shared base contract.

`database/config.json` controls activation state and backend selection. JSON data is stored under `database/json/`; SQLite data is stored under `database/sqlite3/`; MySQL connection settings come from configuration/environment. JSON records and SQLite columns use uppercase field names such as `UUID`, `USERNAME`, `BALANCE`, and `CREATED_AT`.

`src/__init__.py` centralizes shared imports, project URLs, configuration loading, `.env` loading, and common Windows window helpers. Email modules read SMTP credentials from `.env`; use `.env.example` as the variable-name reference and do not commit credentials.

## Repository conventions

- The codebase uses Python 3.15 lazy-import syntax (`lazy import` and `lazy from`); preserve that style rather than converting imports to an older pattern.
- Backend APIs are exposed as class-based namespaces whose methods are generally class methods. Keep method signatures and return shapes consistent with the matching class in `src/__server__/__base__/`.
- Keep persistence-specific SQL, JSON file access, and connection handling inside the selected backend package. Shared UI behavior belongs outside `_json`, `_sqlite3`, and `_mysql`.
- Preserve the existing lower-case class naming convention for UI entry points and components, such as `sign_in_interface`, `sign_up_interface`, and `dashboard_interface`.
- Dashboard and administrator screens are composed from nested UI components. Reuse the existing `SERVER` lookup/management methods and CustomTkinter asset helpers instead of duplicating persistence or asset-loading logic in individual tiles/views.
- Runtime configuration and local data are part of the application’s execution environment. Be careful when changing `database/config.json` or the SQLite/JSON stores; avoid treating generated/runtime state as source code.
- The repository uses four-space indentation, LF line endings, and a final newline as defined in `.editorconfig`. Markdown is exempt from trailing-whitespace trimming.
