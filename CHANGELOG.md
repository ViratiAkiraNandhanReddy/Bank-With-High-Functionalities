# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha.2] - 2026-08-12

### Added

#### Financial Operations

* Deposit functionality with balance and transaction updates
* Withdraw functionality with balance validation and transaction logging
* User-to-user fund transfer functionality
* Transfer-in and transfer-out transaction records
* Transaction counterparty tracking
* Frequent transfer recipient lookup
* Transaction history retrieval

#### Dashboard

* Functional deposit action interface
* Functional withdraw action interface
* Multi-step transfer interface with recipient validation
* Account information tile improvements
* Favorites tile for frequently used transfer recipients
* Announcement tile for application announcements
* Security activity tile for recent account security events
* Transaction history tile with transaction type, amount, counterparty, and timestamp
* Transaction history overlay with a scrollable full-history view
* Security history overlay with a scrollable full-history view
* Support overlay
* Dashboard overlay controls for transactions, security, and support
* Dashboard refresh support for dynamic transaction, favorite, and security data
* Local timezone conversion for displayed transaction and security-event timestamps

#### Security & Authentication

* Security event recording framework
* Login security-event recording
* Failed-login security-event recording
* Logout security-event recording
* Recent security-event lookup
* Security event labels and severity indicators
* Scrollable security-event history
* Improved security overlay event handling

#### Database Architecture

* Expanded authentication base interfaces for password, backup-code, email, and login-time operations
* Expanded user lookup interfaces
* Expanded user management interfaces
* Application announcement lookup and management interfaces
* Security event lookup and management interfaces
* Transaction management interfaces
* Announcement schema support
* Security event schema support
* SQLite implementations for financial operations
* SQLite transaction logging
* SQLite security-event storage and retrieval
* SQLite application announcement storage and retrieval
* UUID-aware user resolution across authentication, lookup, and management operations

#### User Interface & Assets

* Material Design icons for dashboard functionality
* Transaction-related icons
* Security and account-management icons
* Support and recipient-search icons
* Improved dashboard action and overlay interfaces

#### Project Infrastructure

* MIT License
* Release metadata updates
* Updated application packaging and project structure
* Removal of obsolete installer, uninstaller, setup, and deployment artifacts
* Additional README placeholders for generated/runtime directories

### Changed

* Refactored dashboard initialization to support additional tiles and overlays
* Updated transaction display formatting and transaction-type presentation
* Updated security activity presentation
* Improved dashboard navigation and overlay placement
* Extended server abstractions to support the newly implemented application functionality
* Updated SQLite database initialization and schema handling
* Improved account-management operations to work with username or UUID identifiers
* Updated sign-in flow to record authentication security events

### Removed

* Legacy Apache 2.0 license text in favor of the MIT License
* Deprecated setup wizard implementation
* Legacy installer and uninstaller source implementations
* Obsolete setup terms-of-service file
* Obsolete release metadata entries
* Unused deployment and executable-source documentation associated with the previous packaging flow

### Known Limitations

* Email notifications continue to require Gmail SMTP credentials.
* Financial operations are currently implemented in the SQLite backend; equivalent implementations for other database backends remain incomplete.

## [0.1.0-alpha.1] - 2026-07-09

### Added

#### Authentication & Activation
- Product key validation system (development keys)
- Sign-in interface with user session tracking
- Sign-up interface for new account creation
- User and administrator authentication framework
- Backup code authentication support
- Email-based authentication verification

#### Email System
- Welcome email notifications upon account creation
- Forgot password functionality with OTP (One-Time Password) verification
- 10-minute OTP lifetime with countdown timer
- HTML email templates for professional communication
- SMTP Gmail integration for email delivery

#### User Interface
- CustomTkinter-based graphical user interface framework
- Borderless window support with native Win32 drag functionality
- Sign-in and sign-up screens with animated transitions (RTL/LTR)
- Dashboard interface with modular tile system
- Settings overlay for user preferences
- Administrator status panel for system monitoring
- Dashboard tiles:
  - Initial dashboard tile layout
  - Balance tile with transaction trend indicators

#### Database Architecture
- Multi-database backend support with pluggable architecture:
  - JSON database implementation
  - MySQL connector integration
  - SQLite3 support
- Database initialization and connection management for supported backends
- Schema definitions for users, administrators, and transactions
- User and admin lookup base classes
- User and admin management base classes (password/username change, deletion)

#### Backup & Recovery System
- Backup and recovery system (current implementation)
- Three-slot backup rotation mechanism
- Backup detection and validation
- Backup restoration functionality
- Backup metadata retrieval (size, initialization data)

#### Configuration & Environment Management
- JSON-based configuration system for application settings
- python-dotenv support for environment variable management
- Automatic configuration persistence
- Application state tracking (last used timestamps)
- Multi-database type configuration support

#### Security & Privacy
- caesarcipher-extended integration for application data encryption
- Email masking utility for privacy-safe identity confirmation
- User session tracking

#### Utilities & Infrastructure
- Color manipulation utilities for application theming
- Browser integration for URLs and local HTML files
- Network connectivity checking via DNS resolution
- Material Design icon library integration
- Branded application banner assets
- UUID-based user identifiers

#### Project Infrastructure
- Editor configuration (.editorconfig) for code formatting consistency
- Environment example configuration (.env.example)
- Project dependency specification (requirements.txt)
- Apache 2.0 license
- Code of conduct and contributor guidelines
- Security policy documentation
- Support documentation

### Known Limitations
- Windows platform specific (Win32 API, SMTP configuration)
- Email notifications require Gmail SMTP credentials
- The backup and recovery system is functional but based on a deprecated implementation and will be restructured in future releases.
- Core financial operations (deposit, withdraw, transfer, balance inquiry, transaction logging) are architecture-defined but not yet implemented in database backends

[Unreleased]: https://github.com/ZeroMergeConflicts/Bank-With-High-Functionalities/compare/v0.1.0-alpha.2...HEAD
[0.1.0-alpha.1]: https://github.com/ZeroMergeConflicts/Bank-With-High-Functionalities/releases/tag/v0.1.0-alpha.1
[0.1.0-alpha.2]: https://github.com/ZeroMergeConflicts/Bank-With-High-Functionalities/releases/tag/v0.1.0-alpha.2