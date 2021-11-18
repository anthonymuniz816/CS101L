#Anthony Muniz
#Program 11
#CS 101 Lab

#Problem: Need to develop a program that will display the time according to the user's choice.

#ALGORITHM:
#START
#Create class and define parameters
#Create str function within the class
#Ask user for their choice
#If incorrect choice is inputted, ask again until user inputs correct choice
#Ask user for the hour
#If incorrect hour is inputted, ask again until user inputs correct hour
#Ask for the minute
#If incorrect minute is inputted, ask again until user inputs correct minute
#Ask user for the second
#If incorrect second is inputted, ask again until user inputs correct second
#Call the class with the inputs in the main
#Create while loop and print the time
#END

import time
class Clock:
    def __init_(self, hour=0, minute=0, second=0,option=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.option = option

    def __str__(self):
        if self.option == 0:
            return '{:02}:{:02}:{:02}'.format(self.hour,self.minute,self.second)
        elif self.option == 1:
            if self.hour == 12:
                return '{:02}:{:02}:{:02} {}'.format(self.hour,self.minute,self.second,'pm')
            elif self.hour > 12:
                return '{:02}:{:02}:{:02} {}'.format(self.hour-12,self.minute,self.second,'pm')
            elif self.hour < 12:
                return '{:02}:{:02}:{:02} {}'.format(self.hour,self.minute,self.second,'am')



user_option = int(input('What is your option?\n0 = 24 hr clock or 1 = 12 hr clock ==> '))
while user_option:
    if user_option > 1 or user_option < 0:
        print('Enter valid option')
        user_option = int(input('What is your option?\n0 = 24 hr clock or 1 = 12 hr clock ==> '))
    else:
        break
        
user_hour = int(input('What is the current hour ==> '))
while user_hour:
    if user_hour > 24 or user_hour < 0:
        print('Enter a valid hour')
        user_hour = int(input('What is the current hour ==> '))
    else:
        break
        
user_minute = int(input('What is the current minute ==> '))
while user_minute:
    if user_minute < 0 or user_minute > 59:
        print('Enter a valid minute')
        user_minute = int(input('What is the current minute ==> '))
    else:
        break
        
user_second = int(input('What is the current second ==> '))
while user_second:
    if user_second < 0 or user_second > 59:
        print('Enter a valid second')
        user_second = int(input('What is the current second ==> '))
    else:
        break

print()
reloj = Clock()
reloj.hour = user_hour
reloj.minute = user_minute
reloj.second = user_second
reloj.option = user_option

while True:
    print(reloj)
    reloj.second += 1
    time.sleep(1)
    if reloj.second > 59:
        reloj.second = 0
        reloj.minute += 1
    if reloj.minute > 59:
        reloj.minute = 0
        reloj.hour += 1
