import time
import os
from gpiozero import MotionSensor
from datetime import datetime
from smtplib import SMTP
from smtplib import SMTPException
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

pir = MotionSensor(23)

print("Process started")

photo_taking_time = datetime.now().strftime("%a %d %b @ %H:%M")

addressee = "szalaimarci99@gmail.com"
me = "szalaim1999@gmail.com"
subject = 'Motion detected at : ' + photo_taking_time

message = MIMEMultipart()
message['Subject'] = subject
message['From'] = me
message['To'] = addressee
message.preamble = "Warning! " + photo_taking_time



while True:
   if(pir.wait_for_motion()):
      os.system("fswebcam --fps 15 -S 8 -r 640x480 --no-banner --png 9 photo.png")
      print("Motion detected!")

      fp = open('photo.png', 'rb')
      img = MIMEImage(fp.read())
      fp.close()
      message.attach(img)

      time.sleep(5)
      print("Saving image")
      my_smtp = smtplib.SMTP('smtp.gmail.com',587)
      my_smtp.ehlo()
      my_smtp.starttls()
      my_smtp.ehlo()
      my_smtp.login(user = 'szalaim1999@gmail.com',password = 'Jelszóhelye')
      #s.send_message(msg)
      my_smtp.sendmail(me, addressee, message.as_string())
      print("Email has been sent")
      #s.quit()
      time.sleep(5)
   else:
      print("No motion")

