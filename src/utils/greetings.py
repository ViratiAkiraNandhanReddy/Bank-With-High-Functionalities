from datetime import datetime


class greetings:

    @staticmethod
    def current() -> str:

        hour = datetime.now().hour

        if hour < 12:
            return "Good Morning"

        if hour < 17:
            return "Good Afternoon"

        return "Good Evening"
