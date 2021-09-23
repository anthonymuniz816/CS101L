#CS 101L
#Program 2
#Anthony Muniz
#AMMW5@umsystem.edu

#PROBLEM: Need to develop a code that accepts 3 inputed integers and then guesses the number that the user was thinking about
#then asks if the user wants to play again.

#ALGORITHM:
#start
# 1.Print first statement
# 2.user input the remainder of the number that they are thinking about if divided by three,has to be >0 & <the number they are dividing by
# if user input is less than 0, print statement and ask again
# if user input is more than number they are asked to divide, print statement and ask again
# else continue
# 3.for loop for number in the range of 1-100
# 4.if number in range is equal to the user inputs,divided by its respective numbers
# 5.print statement with number guessed correctly
# 6.ask if user wants to play again
# if user says yes, restart game
# if user says something else, ask again
# if user says no, end game
#end 

print('Please think of a number between and including 1 and 100.')
print()
div3=int(input('What is the remainder when your number is divided by 3 ? '))
while div3 < 0 or div3 > 3 or div3 == 3:
    if div3 < 0:
        print('The value entered must be 0 or greater')
        div3=int(input('What is the remainder when your number is divided by 3 ? '))
    elif div3 > 3 or div3 == 3:
        print('The value entered must be less than 3')
        div3=int(input('What is the remainder when your number is divided by 3 ? '))
    else:
        continue    
print()    
div5 = int(input('What is the remainder when your number is divided by 5 ? '))
while div5 < 0 or div5 > 5 or div5 == 5:
    if div5 < 0:
        print('The value entered must be 0 or greater')
        div5=int(input('What is the remainder when your number is divided by 5 ? '))
    elif div5 > 5 or div5 == 5:
        print('The value entered must be less than 5')
        div5=int(input('What is the remainder when your number is divided by 5 ? '))
    else:
        continue    
print()
div7 = int(input('What is the remainder when your number is divided by 7 ? '))
while div7 < 0 or div7 > 7 or div7 == 7:
    if div7 < 0:
        print('The value entered must be 0 or greater')
        div7=int(input('What is the remainder when your number is divided by 7 ? '))
    elif div7 > 7 or div7 == 7:
        print('The value entered must be less than 7')
        div7=int(input('What is the remainder when your number is divided by 7 ? '))
    else:
        continue    
for i in range(1,101):
    if i % 3 == div3 and i % 5 == div5 and i % 7 == div7:
        print('Your number was ',i)
        print('How amazing is that?')
print()
play_again = input('Do you want to play again? Y to continue, N to quit ')
print()
while play_again == 'y' or play_again == 'Y' or play_again == 'n' or play_again == 'N' or play_again != 'y' or play_again != 'Y' or play_again != 'n' or play_again != 'N':
    if play_again == 'n' or play_again == 'N':
        break
    elif play_again == 'y' or play_again == 'Y':
        print('Please think of a number between and including 1 and 100.')
        print()
        div3=int(input('What is the remainder when your number is divided by 3 ? '))
        while div3 < 0 or div3 > 3 or div3 == 3:
            if div3 < 0:
                print('The value entered must be 0 or greater')
                div3=int(input('What is the remainder when your number is divided by 3 ? '))
            elif div3 > 3 or div3 == 3:
                print('The value entered must be less than 3')
                div3=int(input('What is the remainder when your number is divided by 3 ? '))
            else:
                continue    
        print()    
        div5 = int(input('What is the remainder when your number is divided by 5 ? '))
        while div5 < 0 or div5 > 5 or div5 == 5:
            if div5 < 0:
                print('The value entered must be 0 or greater')
                div5=int(input('What is the remainder when your number is divided by 5 ? '))
            elif div5 > 5 or div5 == 5:
                print('The value entered must be less than 5')
                div5=int(input('What is the remainder when your number is divided by 5 ? '))
            else:
                continue    
        print()
        div7 = int(input('What is the remainder when your number is divided by 7 ? '))
        while div7 < 0 or div7 > 7 or div7 == 7:
            if div7 < 0:
                print('The value entered must be 0 or greater')
                div7=int(input('What is the remainder when your number is divided by 7 ? '))
            elif div7 > 7 or div7 == 7:
                print('The value entered must be less than 7')
                div7=int(input('What is the remainder when your number is divided by 7 ? '))
            else:
                continue    
        for i in range(1,101):
            if i % 3 == div3 and i % 5 == div5 and i % 7 == div7:
                print('Your number was ',i)
                print('How amazing is that?')
                print()
        play_again = input('Do you want to play again? Y to continue, N to quit ')
        print()      
    elif play_again != 'n' or play_again != 'N' or play_again != 'y' or play_again != 'Y':
        play_again = input('Do you want to play again? Y to continue, N to  quit ')
        print()
    
