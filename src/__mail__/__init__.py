'''
Docstring for src.__mail__
'''

import os
import smtplib
from random import random, randint
from email.message import EmailMessage as email_msg

DIR_PATH = str(os.environ.get('LOCALAPPDATA')) + r'\Bank-With-High-Functionalities'

SMTP__MAIL_ADDRESS = os.getenv('SMTP__MAIL_ADDRESS')
SMTP__APP_PASSWORD = os.getenv('SMTP__APP_PASSWORD')

otp_code = lambda: str(

    int( random() * ( 999 - 100 ) + 100 )

    ) + chr(

        randint( 65, 90 )

        ) + str(

            int( random() * ( 99 - 11 ) + 11 )

            ) + chr(

                randint( 65, 90 )

                ) + str(

                    int( random() * ( 99 - 11 ) + 11 )

                    ) + chr(

                        randint( 65, 90 )

                        )
