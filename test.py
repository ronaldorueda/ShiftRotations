import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import email.mime.application
import mimetypes

recipients = ['']

msg = MIMEMultipart()
msg['From'] = 'rotationsemail@gmail.com'
msg['To'] = ", ".join(recipients)
msg['Subject'] = 'Here is the new schedule for the following week.'
message = 'Schedule for week of 14-06-2021'
msg.attach(MIMEText(message))

attach_file_name = 'Schedule for the week of 14-06-2021.txt'
fo=open(attach_file_name,'rb')
attach = email.mime.application.MIMEApplication(fo.read(),_subtype="txt")
fo.close()
attach.add_header('Content-Disposition','attachment',filename=attach_file_name)
msg.attach(attach)

mailserver = smtplib.SMTP('smtp.gmail.com',587)
# identify ourselves to smtp gmail client
mailserver.ehlo()
# secure our email with tls encryption
mailserver.starttls()
# re-identify ourselves as an encrypted connection
mailserver.ehlo()
mailserver.login('', '')

mailserver.sendmail('rotationsemail@gmail.com',recipients,msg.as_string())

mailserver.quit()

print("Script complete.")