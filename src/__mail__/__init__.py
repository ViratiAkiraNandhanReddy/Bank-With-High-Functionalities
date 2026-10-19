"""
Docstring for src.__mail__
"""

lazy from ._email_verification import email_verification
lazy from ._forgot_password import forgot_password
lazy from ._two_factor_authentication import two_factor_authentication
lazy from ._welcome import welcome

__all__ = [
    "welcome",
    "forgot_password",
    "email_verification",
    "two_factor_authentication",
]
