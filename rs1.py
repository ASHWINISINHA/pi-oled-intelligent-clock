import time
import os,time
from time import gmtime, strftime

while True:
  showtime = strftime("%A  %d %B %y time %X second",gmtime())
  def female(text):
       os.system("espeak ' " + text + " ' ")
  female(showtime)
  time.sleep(60)
  
