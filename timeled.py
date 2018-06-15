import RPi.GPIO as GPIO
import time
import datetime
GPIO.setmode(GPIO.BOARD)

green = 35
red = 33
blue = 37

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

Freq = 100

RED = GPIO.PWM(red, Freq)
GREEN = GPIO.PWM(green, Freq)
BLUE = GPIO.PWM(blue, Freq)


now = datetime.datetime.now()
today5am = now.replace(hour=5, minute=0, second=0, microsecond=0)
today8am = now.replace(hour=8, minute=0, second=0, microsecond=0)
today12am = now.replace(hour=12, minute=0, second=0, microsecond=0)
today1pm = now.replace(hour=1, minute=0, second=0, microsecond=0)
today3pm = now.replace(hour=3, minute=0, second=0, microsecond=0)
today5pm = now.replace(hour=5, minute=0, second=0, microsecond=0)
today7pm = now.replace(hour=7, minute=0, second=0, microsecond=0)
today8pm = now.replace(hour=8, minute=0, second=0, microsecond=0)
today10pm = now.replace(hour=10, minute=0, second=0, microsecond=0)
while True:
      RED.start(100)
      GREEN.start(1)
      BLUE.start(1)

      if  now == today5am:
          GREEN.ChangeDutyCycle(100)
          RED.ChangeDutyCycle(100)
          BLUE.ChangeDutyCycle(0)
          print ("5")
      if  now > today8am:
          print (  "8")
          GREEN.ChangeDutyCycle(100)
          RED.ChangeDutyCycle(50)
          BLUE.ChangeDutyCycle(50)
      if  now == today12am:
          print ("grater")
          GREEN.ChangeDutyCycle(0)
          RED.ChangeDutyCycle(100)
          BLUE.ChangeDutyCycle(50)
      if  now == today1pm:
          print ("rue")
          GREEN.ChangeDutyCycle(50)
          RED.ChangeDutyCycle(100)
          BLUE.ChangeDutyCycle(0)
      if  now == today3pm:
          print (  "False")
          GREEN.ChangeDutyCycle(50)
          RED.ChangeDutyCycle(100)
          BLUE.ChangeDutyCycle(0)
      if  now == today5pm:
          print ("grater")
          GREEN.ChangeDutyCycle(0)
          RED.ChangeDutyCycle(50)
          BLUE.ChangeDutyCycle(50)
          
      if  now == today7pm:
          ptrin ("True")
          GREEN.ChangeDutyCycle(50)
          RED.ChangeDutyCycle(50)
          BLUE.ChangeDutyCycle(100)
      if  now == today8pm:
          print (  "False")
          GREEN.ChangeDutyCycle(0)
          RED.ChangeDutyCycle(0)
          BLUE.ChangeDutyCycle(0)
          
      if  now == today10pm:
          print ("grater")
          GREEN.ChangeDutyCycle(0)
          RED.ChangeDutyCycle(0)
          BLUE.ChangeDutyCycle(0)
      if  now == today5am:
          print ("True")
          GREEN.ChangeDutyCycle(0)
          RED.ChangeDutyCycle(0)
          BLUE.ChangeDutyCycle(0)

