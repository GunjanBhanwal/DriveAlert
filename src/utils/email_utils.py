import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

def send_email_in_background():
    def send_email():
        from_email = "youremail@example.com"
        from_password = "yourpassword"
        to_email = "recipient@example.com"
        subject = "Alert: Driver Drowsy"
        body = "The driver appears to be drowsy or sleeping. Please take action immediately."

        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_email, from_password)
            text = msg.as_string()
            server.sendmail(from_email, to_email, text)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")

    email_thread = threading.Thread(target=send_email)
    email_thread.start()
