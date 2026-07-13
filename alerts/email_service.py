import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from dotenv import load_dotenv

load_dotenv()


class EmailService:

    def __init__(self):

        self.sender_email = os.getenv("EMAIL_ADDRESS")
        self.sender_password = os.getenv("EMAIL_PASSWORD")

    def send_email(
        self,
        receiver_email,
        subject,
        html_body
    ):

        message = MIMEMultipart("alternative")

        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = receiver_email

        message.attach(
            MIMEText(html_body, "html")
        )

        with smtplib.SMTP("smtp.gmail.com", 587) as server:

            server.starttls()

            server.login(
                self.sender_email,
                self.sender_password
            )

            server.send_message(message)