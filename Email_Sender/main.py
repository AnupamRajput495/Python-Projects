import smtplib
from email.message import EmailMessage
import schedule
import time
from credentials import ID, Pass

EMAIL_ADDRESS = ID
EMAIL_PASSWORD = Pass
To=(str(input("Enter the mail ID")))

def send_email():
    msg = EmailMessage()
    msg["Subject"] = "Automated Email Test"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = To
    msg.set_content("Hello! This is an automated email sent using Python. 🚀")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("✅ Email Sent Successfully!")

schedule.every().day.at("19:03").do(send_email)

print("📢 Email automation started... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(5)