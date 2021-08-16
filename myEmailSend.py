import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.mime.application
import mimetypes

def sendEmail(fileName, fileNameExt):
    recipients = ['']

    msg = MIMEMultipart()
    msg['From'] = 'rotationsemail@gmail.com'
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = 'Here is the new schedule for the following week.'
    message = fileName
    msg.attach(MIMEText(message))

    fo = open(fileNameExt, 'rb')
    attach = email.mime.application.MIMEApplication(fo.read(),_subtype="txt")
    fo.close()
    attach.add_header('Content-Disposition','attachment',filename=fileNameExt)
    msg.attach(attach)

    mailserver = smtplib.SMTP('smtp.gmail.com',587)
    # identify ourselves to smtp gmail client
    mailserver.ehlo()
    # secure our email with tls encryption
    mailserver.starttls()
    # re-identify ourselves as an encrypted connection
    mailserver.ehlo()
    mailserver.login('rotationsemail@gmail.com', '!')

    mailserver.sendmail('rotationsemail@gmail.com',recipients,msg.as_string())

    mailserver.quit()

    return 'Email Sent'

def failedEmail():
    return 'Cannot access SMTP server. Email cannot be sent.'