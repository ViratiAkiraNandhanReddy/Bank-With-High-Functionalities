# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]


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

[Unreleased]: https://github.com/ZeroMergeConflicts/Bank-With-High-Functionalities/compare/v0.1.0-alpha.1...HEAD
[0.1.0-alpha.1]: https://github.com/ZeroMergeConflicts/Bank-With-High-Functionalities/releases/tag/v0.1.0-alpha.1
