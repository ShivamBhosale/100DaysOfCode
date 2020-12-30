""" Sending Mails With Python """
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com",465)
server.ehlo() #Command used to start the process or server

with open('password.txt', 'r') as f: #Create a file password.txt in the same directory with your password in it.
    password = f.read()

server.login('abc123@gmail.com',password)  #Enter youur email and attach your password file

msg = MIMEMultipart()
msg['From'] = 'Shivam Bhosale'
msg['To'] = 'xyz456@gmail.com'
msg["Subject"] = 'This is a test mail send using Python'

with open('message.txt','r') as f:
    message = f.read()

msg.attach(MIMEText(message,'plain'))

filename = 'dog.jpg'
attachment = open(filename,'rb')

p = MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.addheader('Content-Disposition',f'attachement; filename={filename}')
msg.attach(p)

text = msg.as_string()

server.sendmail('abc123@gmail.com','xyz456@gmail.com', text) # From and To mail Ids

print("Mail Send Succesfully")