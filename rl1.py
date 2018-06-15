#Program asks for user input to determine color to shine.

import time, sys
import RPi.GPIO as GPIO

redPin = 35   #Set to appropriate GPIO
greenPin = 33 #Should be set in the 
bluePin = 37 #GPIO.BOARD format

def blink(pin):
    GPIO.setmode(GPIO.BOARD)
    
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)
    
def turnOff(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    
def redOn():
    blink(redPin)

def redOff():
    turnOff(redPin)

def greenOn():
    blink(greenPin)

def greenOff():
    turnOff(greenPin)

def blueOn():
    blink(bluePin)

def blueOff():
    turnOff(bluePin)

def yellowOn():
    blink(redPin)
    blink(greenPin)

def yellowOff():
    turnOff(redPin)
    turnOff(greenPin)

def cyanOn():
    blink(greenPin)
    blink(bluePin)

def cyanOff():
    turnOff(greenPin)
    turnOff(bluePin)

def magentaOn():
    blink(redPin)
    blink(bluePin)

def magentaOff():
    turnOff(redPin)
    turnOff(bluePin)

def whiteOn():
    blink(redPin)
    blink(greenPin)
    blink(bluePin)

def whiteOff():
    turnOff(redPin)
    turnOff(greenPin)
    turnOff(bluePin)
    
def main():
    while True:
        redOn()
        time.sleep(1)
        greenOn()
        time.sleep(1)
        blueOn()
        time.sleep(1)
        yellowOn()
        time.sleep(1)
        cyanOn()
        time.sleep(1)
        magentaOn()
        time.sleep(1)
        whiteOn()
        time.sleep(1)
        
        
        
        
    return
    

main()
    
