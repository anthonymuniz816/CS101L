#CS 101 Lab
#Program 5
#Name: Anthony Muniz
#Email: AMMW5@umsystem.edu

#Problem: Need to develop a code that requires a user input and will return the students school and grade if valid,
#and return invalid along with the issue if the input is invalid.

#ALGORITHM:
#start
#Print Header for program formatted
#Make a while true statement
#Ask user to input card number
#If user doesn't input anything, end program
#If user input is valid and returns true in the verify_get_check function
#Print that the input is valid, along with the students school and grade, and ask for user input again
#If the user input is invalid and returns False in the verify_get_check function
#Print that the user input is invalid, along with why it is invalid and ask for user input again
#Iterate until user inputs nothing

import string
def get_school(sid):
    while get_school:
        if sid[5] == '1':
            return('School of Computing and Engineering SCE.')
            break
        elif sid[5] == '2':
            return('School of Law.')
            break
        elif sid[5] == '3':
            return('College of Arts and Sciences.')
            break
        else:
            return('Invalid school.')
            break

def get_grade(sid):
    while get_grade:
        if sid[6] == '1':
            return('Freshman.')
            break
        elif sid[6] == '2':
            return('Sophomore.')
            break
        elif sid[6] == '3':
            return('Junior.')
            break
        elif sid[6] == '4':
            return('Senior.')
            break
        else:
            print('Invalid grade.')
            break

def character_value(sid):
    id1= string.ascii_uppercase.index(sid[0])
    id2= string.ascii_uppercase.index(sid[1])
    id3= string.ascii_uppercase.index(sid[2])
    id4= string.ascii_uppercase.index(sid[3])
    id5= string.ascii_uppercase.index(sid[4])
    return id1,id2,id3,id4,int(id5), int(sid[5]), int(sid[6]), int(sid[7]), int(sid[8]), int(sid[9])

def get_check_digit(character_value):
    num1 = character_value[0] * 1
    num2 = character_value[0] * 2
    num3 = character_value[0] * 3
    num4 = character_value[0] * 4
    num5 = character_value[0] * 5
    num6 = character_value[0] * 6
    num7 = character_value[0] * 7
    num8 = character_value[0] * 8
    num9 = character_value[0] * 9
    return (num1+num2+num3+num4+num5+num6+num7+num8+num9)%10

def verify_check_digit(sid):
   
    while verify_check_digit:
        if len(sid) != 10:
            print('Libary card is invalid.')
            print('The length of the number given must be 10')
            return False
        elif sid[0].isalpha() == False:
            print("Libary card is invalid.")
            print('The first 5 characters must be A-Z, the invalid character is at 1 is %s'%sid[0])
            return False
        elif sid[1].isalpha() == False:
            print("Libary card is invalid.")
            print('The first 5 characters must be A-Z, the invalid character is at 2 is %s'%sid[1])
            return False
        elif sid[2].isalpha() == False:
            print("Libary card is invalid.")
            print('The first 5 characters must be A-Z, the invalid character is at 3 is %s'%sid[2])
            return False
        elif sid[3].isalpha() == False:
            print("Libary card is invalid.")
            print('The first 5 characters must be A-Z, the invalid character is at 4 is %s'%sid[3])
            return False
        elif sid[4].isalpha() == False:
            print("Libary card is invalid.")
            print('The first 5 characters must be A-Z, the invalid character is at 5 is %s'%sid[4])
            return False
        elif sid[7].isalnum() == False:
            print("Libary card is invalid.")
            print('The last 3 characters must be 0-9, the invalid character is at 7 is %s'%sid[7])
            return False
        elif sid[8].isalnum() == False:
            print("Libary card is invalid.")
            print('The last 3 characters must be 0-9, the invalid character is at 7 is %s'%sid[8])
            return False
        elif sid[9].isalnum() == False:
            print("Libary card is invalid.")
            print('The last 3 characters must be 0-9, the invalid character is at 7 is %s'%sid[9])
            return False
        elif int(sid[5]) > 3:
            print("Libary card is invalid.")
            print('The sixth character must be 1 2 or 3')
            return False
        elif int(sid[6]) > 4:
            print("Libary card is invalid.")
            print('The seventh character must be 1 2 3 or 4')
            return False
        elif int(get_check_digit(character_value(sid))) != int(sid[9]):
            print('Library card is invalid.')
            print('Check Digit does not match calculated value')
            return False
        else:
            return True
        
      
        

               
if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)
    
    while True:

        print()
        card_num = input("Enter Libary Card.  Hit Enter to Exit ==> ").upper()
        
        
    
        if card_num == "":
            break
        
    
        if verify_check_digit(card_num) == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            continue
