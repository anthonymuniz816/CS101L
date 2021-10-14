#CS 101 Lab
#Program 5
#Name: Anthony Muniz
#Email: AMMW5@umsystem.edu

#PROBLEM: Need to develop a code that takes in a user input and then encodes or
#decodes the input depending on the user's selection.

#ALGORITHM:
#start
#Make a while while lopp and set to True
#Print header for program formatted
#Ask for user's selection based on the printed header
#If user inputs 1, the program will ask for the user to enter a string & print a encoded version
#If the user inputs 2, the program will ask for the user to enter a string & print a decoded version
#If the user inputs Q, the program will end
#If the user inputs something else, the program will ask again until a valid input is inputted
#end


while True:
    print()
    print('Main Menu:')
    print('1) Encode a string')
    print('2) Decode a string')
    print('Q) Quit')
    selection = input('Enter your selection ==> ')
    if selection == 'Q' or selection == 'q': #Ends program
        print('Have a great day')
        break
    
    elif selection == '1': #Encodes string
        user_text = input('Enter (brief) text to decrypt: ')
        shift_amount = int(input('Enter the number to shift letters by: '))
        for i in user_text:
            if i == ' ':
                i = ' '
                print(i, end='')
            else:
                new_ord=ord(i)+ shift_amount
                new_chr=chr(new_ord).upper()
                print(new_chr, end='')
        print()
            
    elif selection == '2': #Decodes string
        user_text = input('Enter (brief) text to decrypt: ')
        shift_amount = int(input('Enter the number to shift letters by: '))
        for i in user_text:
            if i == ' ':
                i = ' '
                print(i, end='')
            else:
                new_ord=ord(i) - shift_amount
                new_chr=chr(new_ord).upper()
                print(new_chr, end='')
        print()
       






