import RPi.GPIO as GPIO  
from time import sleep     # this lets us have a time delay (see line 15)  
GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering  
GPIO.setup(4, GPIO.IN)    # set GPIO25 as input (button)  
GPIO.setup(8, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(9, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(10, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(11, GPIO.IN, GPIO.PUD_DOWN)
  
try:  
    while True:            
        if GPIO.input(8): 
            print("GPIO8 HIGH" ) 
        if GPIO.input(9): 
            print("GPIO9 HIGH" ) 
        if GPIO.input(10): 
            print("GPIO10 HIGH" ) 
        if GPIO.input(11): 
            print("GPIO11 HIGH" ) 
                
  
finally:                   # this block will run no matter how the try block exits  
    GPIO.cleanup() 
