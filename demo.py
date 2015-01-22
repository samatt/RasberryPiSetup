# print "Hello World"

import RPi.GPIO as GPIO  
import time  

def blink(pin):  
	print "GPIO " + str(pin) + " HIGH"
	GPIO.output(pin,GPIO.HIGH)
	time.sleep(1)  
	GPIO.output(pin,GPIO.LOW) 
	print "GPIO " + str(pin) + " LOW" 
	time.sleep(1)  
	return  

print "Hello World"
# to use Raspberry Pi board pin numbers  
GPIO.setmode(GPIO.BOARD)  
# set up GPIO output channel  
GPIO.setup(7, GPIO.OUT)  
# blink GPIO17 50 times  
for i in range(0,50):  
        blink(7)  
GPIO.cleanup()   