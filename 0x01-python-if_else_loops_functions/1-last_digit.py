#!/usr/bin/python3
import random 

number  = random.randint(-10000,10000)
last = number % 10

if last:
    if last in range(-10,0):
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,last))    
    elif last in range(1,6):
        print("Last digit of {} is {} and is less than 6 and not 0".format(number,last))
    elif last  in range(6,10):
        print("Last digit of {} is {} and is greater than 5".format(number,last))
    elif last == 0:
        print("Last digit of {} is {} and is  0".format(number,last))
        
