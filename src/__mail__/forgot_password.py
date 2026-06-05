from ._imports import *


class forgot_password:

    def __init__(
        self,
        receiver_mail_address: str,
        ctk_report: tuple[
            CTkLabel, int, int, str, str
        ],  # (CTkLabel, x, y, success_msg, error_msg)
        receiver_type: str = "User",
    ) -> None:

        self.receiver_mail_address: str = receiver_mail_address
        self.ctk_report: tuple[CTkLabel, int, int, str, str] = ctk_report
        self.receiver_type: str = receiver_type

        self.countdown_timer: str

        self._time_on_sent: datetime.datetime

    def send_mail(self) -> None:

        self.otp: str = otp_code()

        with open(
            root / "src" / "__mail__" / "templates" / "forgot_password.html"
        ) as file:

            self.email_html = (
                file.read()
                .replace("[CODE]", self.otp)
                .replace("[EMAIL]", self.receiver_mail_address)
                .replace("[TYPE]", self.receiver_type)
            )

        self.email = email_msg()

        self.email["Subject"] = (
            f"{self.otp} is your verification code to reset password at Bank With High Functionalities."
        )
        self.email["From"] = "Bank With High Functionalities"
        self.email["To"] = self.receiver_mail_address

        self.email.set_content(self.email_html, subtype="html")

        try:

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as gmail:

                gmail.login(f"{SMTP__MAIL_ADDRESS}", f"{SMTP__APP_PASSWORD}")
                gmail.send_message(self.email)

                self._time_on_sent = datetime.datetime.now()

                self.ctk_report[0].after(
                    0,
                    lambda: (
                        self.ctk_report[0].place(
                            x=self.ctk_report[1], y=self.ctk_report[2]
                        ),
                        self.ctk_report[0].configure(text=self.ctk_report[3]),
                        self.ctk_report[0].after(3000, self.ctk_report[0].place_forget),
                    ),
                )
        except Exception as e:
            self.ctk_report[0].after(
                0,
                lambda: (
                    self.ctk_report[0].place(
                        x=self.ctk_report[1], y=self.ctk_report[2]
                    ),
                    self.ctk_report[0].configure(text=self.ctk_report[4]),
                    self.ctk_report[0].after(3000, self.ctk_report[0].place_forget),
                ),
            )

    def start_timer(
        self,
        ctk_instance: CTkLabel | CTkButton,
        ctk_report: tuple[CTkLabel, int, int],
        seconds: int = 600,
    ) -> None:

        mins, secs = divmod(seconds, 60)
        ctk_instance.configure(text=f"{mins:02d}:{secs:02d}")

        if seconds > 0:

            # < recursion > (asynchronously)
            self.countdown_timer: str = ctk_instance.after(
                1000, self.start_timer, ctk_instance, ctk_report, seconds - 1
            )

        else:
            ctk_report[0].place(x=ctk_report[1], y=ctk_report[2])
            ctk_report[0].after(3000, ctk_report[0].place_forget)

            self.send_mail()

    def stop_timer(self, ctk_instance: CTkLabel | CTkButton) -> None:
        ctk_instance.after_cancel(self.countdown_timer)

    def validate_code(self, code: str) -> bool:
        time_elapsed = (datetime.datetime.now() - self._time_on_sent).total_seconds()

        if code == self.otp and time_elapsed <= 600:
            return True

        return False
