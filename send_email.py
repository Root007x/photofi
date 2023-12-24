import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class SendEmail:

    def __init__(self,sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port, smtp_username, smtp_password):

        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.body = body
        self.attachment_path = attachment_path
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.smtp_username = smtp_username
        self.smtp_password = smtp_password
        

    def send_email(self):
        # Create the email message
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.receiver_email
        message['Subject'] = self.subject

        # Attach body text
        message.attach(MIMEText(self.body, 'plain'))

        # Attach the file
        attachment = open(self.attachment_path, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {self.attachment_path}')
        message.attach(part)

        # Connect to the SMTP server and send the email
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_username, self.smtp_password)
            server.sendmail(self.sender_email, self.receiver_email, message.as_string())


