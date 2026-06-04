# Your goal is to implement a function, send_email(), that takes three input arguments for 
# the recipient’s email address, the email’s subject line, and the email message body.

# The 'smtplib' module in Python provides functions and classes for sending emails using the Simple Mail Transfer Protocol (SMTP). 
# By importing 'smtplib', you gain access to the tools needed to establish a connection with an email server and programmatically send email messages.
import smtplib

SENDER_EMAIL = 'dkolomy@hotmail.com'
SENDER_PASSWORD = 'Dmitry1234567890'

def send_email(recipient_email, subject, body):
  message = f"Subject: {subject}\n\n{body}"
  with smtplib.SMTP('smtp.office365.com', 587) as server:
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, recipient_email, message)

send_email('dkolomy@hotmail.com', 'Test Email', 'This is a test email')