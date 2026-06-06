from ._imports import *


class forgot_password:

    OTP_LIFETIME: int = 600  # 10 minutes in seconds

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

        self.timer_id: str

        self.sent_at: datetime.datetime | None = None

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

                # gmail.login(f"{SMTP__MAIL_ADDRESS}", f"{SMTP__APP_PASSWORD}")
                # gmail.send_message(self.email)

                self.sent_at = datetime.datetime.now()

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
        timer_widget: CTkLabel | CTkButton,
        report_widget: tuple[CTkLabel, int, int],
        resend_callback,
        remaining_seconds: int = OTP_LIFETIME,
    ) -> None:

        minutes, seconds = divmod(remaining_seconds, 60)
        timer_widget.configure(text=f"{minutes:02d}:{seconds:02d}")

        if remaining_seconds > 0:
            self.timer_id = timer_widget.after(
                1000,
                self.start_timer,
                timer_widget,
                report_widget,
                resend_callback,
                remaining_seconds - 1,
            )
            return

        report_label, x, y = report_widget

        report_label.place(x=x, y=y)
        report_label.configure(text="OTP expired. A new OTP has been sent.")
        report_label.after(3000, report_label.place_forget)

        resend_callback()

        self.start_timer(
            timer_widget,
            report_widget,
            resend_callback,
            self.OTP_LIFETIME,
        )

    def stop_timer(self, ctk_instance: CTkLabel | CTkButton) -> None:
        ctk_instance.after_cancel(self.timer_id)

    def validate_code(self, code: str) -> bool:

        if self.sent_at is None:
            return False

        elapsed_seconds = (datetime.datetime.now() - self.sent_at).total_seconds()

        return code == self.otp and elapsed_seconds <= self.OTP_LIFETIME
