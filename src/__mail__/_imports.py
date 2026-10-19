lazy import datetime
lazy import os
lazy import smtplib
lazy from email.message import EmailMessage as email_msg
lazy from random import randint, random

lazy from customtkinter import CTkButton, CTkLabel

lazy from ..utils import root

SMTP__MAIL_ADDRESS: str | None = os.getenv("SMTP__MAIL_ADDRESS")
SMTP__APP_PASSWORD: str | None = os.getenv("SMTP__APP_PASSWORD")

otp_code = (
    lambda: str(int(random() * (999 - 100) + 100))
    + chr(randint(65, 90))
    + str(int(random() * (99 - 11) + 11))
    + chr(randint(65, 90))
    + str(int(random() * (99 - 11) + 11))
    + chr(randint(65, 90))
)
