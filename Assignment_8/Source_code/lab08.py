#CS 101 Lab
#Program 8
#Name: Anthony Muniz
#Email: AMMW5@umsystem.edu

#PROBLEM: Need to develop a code that will add, remove, and clear assignments or tests depending on what the user wants to do and will
#also display them if the user wants the information displayed.

#ALGORITHM:
#START
#Import math module
#Create two empty lists, one for tests and one for assignments
#Create a while loop
#Print the Menu options for the user
#Ask user to choose option
#If user inputs 1, ask the user to input a new test score they want added to the list, input must be greater than 0, and repeat step 5
#If user inputs 2, ask user to input the test score they want to remove, if test is not in list then print a statement, and repeat step 5
#If user inputs 3, clear all the items in the tests list, and repeat step 5
#If user inputs 4, ask user to input a new assignment they want added to the list, input must be greater than 0, and repeat step 5
#If user inputs 5, ask the user to input assignment they want removed, if assignment not in list then print statement, and repeat step 5
#If user inputs 6, clear all the items in the assignments list, and repeat step 5
#If user inputs D, display all of the information, and repeat step 5
#If user inputs Q, break and end program
#If user inputs something else, ask user to choose a valid option until valid input is inputted


import math
test_scores = []
assignment_scores = []

while True:
    print()
    print('{:^35}'.format('Grade Menu'))
    print('1 - Add Test')
    print('2 - Remove Test')
    print('3 - Clear Tests')
    print('4 - Add Assignment')
    print('5 - Remove Assignment')
    print('6 - Clear Assignments')
    print('D - Display Scores')
    print('Q - Quit')
    print()
    choice = input('==> ')
    if choice == '1':
        new_test = float(input('Enter the new test score 0-100 ==> '))
        if new_test < 0:
            print('New test score must be greater than 0')
        else:
            test_scores.append(new_test)
    elif choice == '2':
        remove_test = float(input('Enter the test score to remove 0-100 ==>'))
        if remove_test not in test_scores:
            print('Could not find score to remove')
        else:
            test_scores.remove(remove_test)
    elif choice == '3':
        test_scores.clear()
    elif choice == '4':
        new_assignment = float(input('Enter the new assignment score 0-100 ==>'))
        if new_assignment < 0:
            print('New assignment score must be greater than 0')
        else:
            assignment_scores.append(new_assignment)
    elif choice == '5':
        remove_assignment = float(input('Enter the assignment to remove 0-100 ==>'))
        if remove_assignment not in assignment_scores:
            print('Could not find assignment to remove')
        else:
            assignment_scores.remove(remove_assignment)
    elif choice == '6':
        assignment_scores.clear()
    elif choice == 'D' or choice == 'd':
        print('{}{:>16}{:>10}{:>10}{:>10}{:>10}'.format('Type','#','min','max','avg','std'))
        print('='*60)
        if test_scores == []:
            amount_test = 'n/a'
            min_test = 'n/a'
            max_test = 'n/a'
            avg_test = 'n/a'
            std_test = 'n/a'
        else:
            amount_test = len(test_scores)
            min_test = min(test_scores)
            max_test = max(test_scores)
            avg_test = sum(test_scores)/amount_test
            teststd = []
            for i in test_scores:
                num= (i-avg_test)**2
                teststd.append(num)
            std_test = ('%.2f'%(math.sqrt((sum(teststd)/amount_test))))
        if assignment_scores == []:
            amount_assignment = 'n/a'
            min_assignment = 'n/a'
            max_assignment = 'n/a'
            avg_assignment = 'n/a'
            std_assignment = 'n/a'
        else:
            amount_assignment = len(assignment_scores)
            min_assignment = min(assignment_scores)
            max_assignment = max(assignment_scores)
            avg_assignment = sum(assignment_scores)/amount_assignment
            assignmentstd = []
            for i in assignment_scores:
                num2= (i-avg_assignment)**2
                assignmentstd.append(num2)
            std_assignment = ('%.2f'%(math.sqrt((sum(assignmentstd)/amount_assignment))))

        print('{}{:>16}{:>10}{:>10}{:>10}{:>10}'.format('Tests',amount_test,min_test,max_test,avg_test,std_test))
        print('{}{:>13}{:>10}{:>10}{:>10}{:>10}'.format('Programs',amount_assignment,min_assignment,max_assignment,avg_assignment,std_assignment))
        print()
        if test_scores == [] or assignment_scores == []:
            weighted = 0
        else:
            weighted = (avg_test*0.6) + (avg_assignment*0.4)
        print('The weighed scores is {:.2f}'.format(weighted))
    elif choice == 'Q' or choice == 'q':
        print('Have a great day!')
        break
    else:
        print('Enter valid option')
        continue
