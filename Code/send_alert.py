import smtplib
from email.mime.text import MIMEText

def send_email(name, temp):
    body = f"Alert! {name} has a high temperature: {temp:.2f}C"
    msg = MIMEText(body)
    msg["Subject"] = "Covid Alert - Temperature"
    msg["From"] = "sender@example.com"
    msg["To"] = "admin@example.com"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("sender@example.com", "your-password")
        server.send_message(msg)

# Example use
send_email("Ramya", 38.7)