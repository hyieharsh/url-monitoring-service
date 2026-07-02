import smtplib
from email.message import EmailMessage
from config import Config


def send_email_alert(monitor):
    try:
        msg = EmailMessage()

        msg["Subject"] = f"Website Down Alert: {monitor.name}"
        msg["From"] = Config.EMAIL_ADDRESS
        msg["To"] = Config.EMAIL_ADDRESS

        msg.set_content(
            f"""
Website Down Alert!

Website: {monitor.name}
URL: {monitor.url}
Status: DOWN
Time: {monitor.last_checked}
"""
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(
                Config.EMAIL_ADDRESS,
                Config.EMAIL_PASSWORD
            )

            smtp.send_message(msg)

        print(f"Email sent for {monitor.name}")

    except Exception as e:
        print("Email Error:", e)