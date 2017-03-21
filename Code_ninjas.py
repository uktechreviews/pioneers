#This bit is set up by Mr Organ our mentor
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

pin = 17
pin2 = 18

GPIO.setup(pin,GPIO.OUT)
GPIO.setup(pin2,GPIO.OUT)
GPIO.setwarnings(False)

#This is our code from here


print("")
print ("")
print("")
print("")
print("")
print("")
print("")
print("")



print ("We are team >CodeNinjas_")
print ("We want to make you laugh!")
print ("What is your name?")
name = input()

print ("Do you like Minecraft TNT?")
time.sleep(5)

print ("5")
time.sleep(1)
print ("4")
time.sleep(1)
print ("3")
time.sleep(1)
print ("2")
time.sleep(1)
print ("1")



GPIO.output(pin,1)
time.sleep(10)
GPIO.output(pin,0)

print ("You have been pranked " + name)
print ("Ha Ha Ha Ha Ha")


