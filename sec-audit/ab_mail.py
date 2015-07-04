import smtplib
import datetime
import os
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
import glob

fromadd = "prawins2@gmail.com"
toadd = ['sudipshrestha@lftechnology.com', 'prabinsubedi@lftechnology.com','rkapali@lftechnology.com']
now = datetime.datetime.now()
msg = MIMEMultipart('alternative')
part = MIMEApplication(open("/home/gambit/sec-audit/*.pdf", "rb").read())
part.add_header('Content-Disposition', 'attachment', filename="test.txt")
msg.attach(part)
msg['Subject'] = "Hi : Absolute " + now.strftime('%Y/%m/%d')
msg['From'] = fromadd 
msg['To'] = ", ".join(toadd)
text = "I have successfully sendmail:"+ now.strftime('%Y/%m/%d')
part1 = MIMEText(text, 'plain') 
msg.attach(part1)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('prawins2@gmail.com', 'DELL1234')
mail.sendmail(fromadd, toadd, msg.as_string())
#print "mail send with attachment"
mail.quit()

	
	
