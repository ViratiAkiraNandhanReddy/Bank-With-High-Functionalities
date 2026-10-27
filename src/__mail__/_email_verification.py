lazy from ._imports import (
    SMTP__APP_PASSWORD,
    SMTP__MAIL_ADDRESS,
    CTkButton,
    CTkLabel,
    datetime,
    email_msg,
    otp_code,
    randint,
    random,
    root,
    smtplib,
)


class email_verification:

    def __init__(self, receiver_mail_address: str) -> None:

        self.sent: bool = False
        self.otp: str = otp_code()

        with open(
            root / "src" / "__mail__" / "templates" / "email_verification.html"
        ) as file:

            self.email_html = (
                file.read()
                .replace("[CODE]", self.otp)
                .replace("[EMAIL]", receiver_mail_address)
            )

        self.email = email_msg()

        self.email["Subject"] = (
            f"{self.otp} is your code to verify email at Bank With High Functionalities."
        )
        self.email["From"] = "Bank With High Functionalities"
        self.email["To"] = receiver_mail_address

        self.email.set_content(self.email_html, subtype="html")

        try:

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as gmail:

                gmail.login(f"{SMTP__MAIL_ADDRESS}", f"{SMTP__APP_PASSWORD}")
                gmail.send_message(self.email)

                self.sent = True

        except Exception:
            self.sent = False
