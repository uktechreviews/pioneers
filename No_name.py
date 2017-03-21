#This bit is set up by our mentor Mr Organ
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pin = 17
pin2 = 18

GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)

#This is our code

print ("#no_name")

print ("Free cake!")
print ("what is your name?  ")
name = input()
print("hahahahaha ")
print("the cake is a pie ")
print("pranked you " + name)

GPIO.output(pin,0)
time.sleep(2)
GPIO.output(pin,1)
GPIO.output(pin2,0)
time.sleep(2)
GPIO.output(pin2,1)


