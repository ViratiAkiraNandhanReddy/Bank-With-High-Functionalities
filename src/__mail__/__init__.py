"""
Docstring for src.__mail__
"""

from ._welcome import welcome
from ._forgot_password import forgot_password
from ._email_verification import email_verification
from ._two_factor_authentication import two_factor_authentication

__all__ = [
    "welcome",
    "forgot_password",
    "email_verification",
    "two_factor_authentication",
]
