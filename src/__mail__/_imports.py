import os
import smtplib
import datetime
from ..utils import root
from random import random, randint
from customtkinter import CTkButton, CTkLabel
from email.message import EmailMessage as email_msg

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
