from . import *
import datetime

class two_factor_authentication:

    def __init__(self, receiver_mail_address: str) -> None:

        self.otp: str = otp_code()
        
        with open(fr'{DIR_PATH}\src\__mail__\templates\two_factor_authentication.html') as file:
            
            self.email_html = file.read()\
                .replace('[CODE]', self.otp)\
                .replace('[EMAIL]', receiver_mail_address)\
                .replace('[TIME]', datetime.datetime.now().strftime("%I:%M %p"))
        
        self.email = email_msg()

        self.email['Subject'] = f'{self.otp} is your 2FA code to login at Bank With High Functionalities.'
        self.email['From'] = 'Bank With High Functionalities'
        self.email['To'] = receiver_mail_address

        self.email.set_content(self.email_html, subtype='html')


        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail:

                gmail.login(f"{SMTP__MAIL_ADDRESS}", f"{SMTP__APP_PASSWORD}")
                gmail.send_message(self.email)

        except Exception as e:
            ...