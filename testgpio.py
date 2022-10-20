import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN)    # set GPIO25 as input (button)  
# set GPIO24 as an output (LED)  
  
try:  
    while True:            # this will carry on until you hit CTRL+C  
        if GPIO.input(4) == 0: # if port 25 == 1  
            print ("Port 4 low") 
               # wait 0.1 seconds  
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup() 
