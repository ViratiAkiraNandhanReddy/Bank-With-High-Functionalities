"""
Docstring for src.__mail__
"""

from .welcome import welcome
from .forgot_password import forgot_password
from .email_verification import email_verification
from .two_factor_authentication import two_factor_authentication

__all__ = [
    "welcome",
    "forgot_password",
    "email_verification",
    "two_factor_authentication",
]
