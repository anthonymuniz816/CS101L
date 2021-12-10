#Anthony Muniz
#Program 13
#CS 101 Lab

#ALGORITHM:
#START
#Create function that will return the sum of a list
#Create a function that will return the average of a list
#Create a function that will return the median of a list
#END

import math

def total(x):
    total = 0
    for i in x:
        total = total + i
    return float(total)

def average(x):
    if len(x) == 0:
        return math.nan
    return float(total(x) / len(x))

def median(x):
        if x == []:
            raise ValueError
        new = sorted(x)
        n = len(new)
        if n % 2 == 0:
            med = new[n//2]
            med2 = new[n//2 -1]
            median = (med + med2) / 2
        else:
            median = new[n//2]
        return median


