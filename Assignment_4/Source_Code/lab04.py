#CS 101 Lab
#Program 4
#Anthony Muniz
#AMMW5@umsystem.edu

#Problem: Need to develop a slot machine type program, where it asks the user how many
#chips it wants to start out with along with how many chips it wants to wager. The user
#will gain/lose chips according to how many numbers match on the slot machine. The game
#will iterate until user is left without chips and ask him if he wants to play again.

#ALGORITHM:
#1.start
#2.Create playing variable and set it to True
#3.Create while loop for while playing is True
#4.Create bank variable for get_bank function
#Bank variable will ask user how many chips does it want to start with
#5.If user inputs a number higher than 100 or lower than zero, user 
#will be asked to input another number until it is within correct range
#6.Create spins variable and set to zero
#7.Create chips variable that equals bank
#8.Create and empty list that will collect all of the bank results
#9.Create wager variable for get_wager function
#Wager variable will ask user how many chips does it want to wager,
#must be equal to or less than bank
#10.Create variable for get_slot_results, which will return 3 random numbers
#11.Create varibale for get_matches, which will return number of matches
#12.Print spin using get_slot_results function
#13.Print how many numbers matched
#14.Print how much user won or lost depending on their wager
#15.Print their current bank + or - how much they won/lost
#16.Add one to spins variable
#17.Iterate steps 4-16 until user is out of total chips
#18.If user is out of chips, ask user if they want to play again
#If user inputs yes, repeat steps 4-18
#If user inputs no, end game
#If user inputs something else, ask again



import random

def play_again():
    play = True
    while play_again:
        user_input = input('Do you want to play again? ')
        if user_input.upper() == 'Y' or user_input.upper() == 'YES':
            return True
        elif user_input.upper() == 'N' or user_input.upper() == 'NO':
            return False
        else:
            print('You must enter Y/YES/N/NO to continue. Please try again')
            continue

            
def get_wager(bank):
    
    while get_wager:
        user_wager = int(input('How many chips do you want to wager? '))
        if user_wager > bank:
            print('The wager amount cannot be greater than how much you have.', bank)
            user_wager = int(input('How many chips do you want to wager? '))
        elif user_wager <= 0:
            print('The wager amount must be greater than 0. Please enter again.')
            user_wager = int(input('How many chips do you want to wager? '))
        else:
            return user_wager

        
def get_slot_results():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    num3 = random.randint(1,10)
    return num1, num2, num3


def get_matches(reela, reelb, reelc):
    if reela == reelb and reela == reelc:
        return 3
    elif (reela == reelb) or (reela ==reelc) or (reelb == reelc):
        return 2
    else:
        return 0


def get_bank():
    chip = int(input('How many chips do you want to start with? '))
    while chip < 0 or chip > 100 or chip in range(1,101):
        if chip < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
            chip = int(input('How many chips do you want to start with? '))
        elif chip > 101:
            print('Too high a value, you can only choose 1 - 100 chips')
            chip = int(input('How many chips do you want to start with? '))
        else:
            return chip


def get_payout(wager,matches):
    if matches == 3:
        payout = (wager * 10) - wager
    elif matches == 2:
        payout = (wager * 3) - wager
    elif matches == 0:
        payout =  wager * -1
    return payout


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        spins = 0
        chips = bank
        bank_list = []
        while bank > 0:  
            
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            bank_list.append(bank)
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            spins += 1
        
           
        print("You lost all", chips, "in", spins, "spins")
        print("The most chips you had was", max(bank_list))
        playing = play_again()
        
