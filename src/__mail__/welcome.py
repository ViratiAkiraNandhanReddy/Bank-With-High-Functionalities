from . import *

class welcome:

    def __init__(self, receiver_mail_address: str, fullname: str) -> None:
        
        with open(fr'{DIR_PATH}\src\__mail__\templates\welcome.html') as file:
            self.email_html = file.read().replace('[TESTER]', fullname)
        
        self.email = email_msg()

        self.email['Subject'] = 'Welcome to Bank With High Functionalities.'
        self.email['From'] = 'Bank With High Functionalities'
        self.email['To'] = receiver_mail_address

        self.email.set_content(self.email_html, subtype='html')


        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail:

                gmail.login(f"{SMTP__MAIL_ADDRESS}", f"{SMTP__APP_PASSWORD}")
                gmail.send_message(self.email)

        except Exception as e:
            ...