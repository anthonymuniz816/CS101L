#CS 101L
#Program 2
#Anthony Muniz
#AMMW5@umsystem.edu

#PROBLEM: Need to develop a code that calculates the weighted grade for grades of lab, exam and attendace inputed,
#keeping in mind that if the user inputs an input greater than 100 then the input will change to 100 and if the user
#inputs a number less than 0 then the input will change to 0

#Algorithm:
#start
#print header
#add user inputs
#add if & elif statements on every user input apart from the 'name' to examine the user input
#add calculation for weighted
#start 'grade' with 'A'
#add if & elif statements depending on what the weighted grade is corresponding with a letter grade
#print statemnts of the weighted grade corresponding with a letter grade
#print footer
#end

print('**** Welcome to the LAB grade calculator! ****')
print()
name = input('Who are we calculating for? ')
print()
lab = int(input('Enter the Labs grade? '))
#if_elif statements for possible outcomes of grades inputed
if lab < 0:
    lab = 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
elif lab > 100:
    lab = 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
print()
exam = int(input('Enter the EXAMS grade? '))
if exam < 0:
    exam = 0
    print('The exam value should have been zero or greater. It has been changed to zero.')
elif exam > 100:
    exam = 100
    print('The exam value should have been 100 or less. It has been changed to 100.')
print()
attendance = int(input('Enter the Attendance grade? '))
if attendance < 0:
    attendance = 0
    print('The attendance value should have been zero or greater. It has been changed to zero.')
elif attendance > 100:
    attendance = 100
    print('The attendance value should have been 100 or less. It has been changed to 100.')
print()

weighted = float((lab * 0.7) + (exam * 0.2) + (attendance * 0.1)) #main calculation
grade = 'A' #starts with A and will change depending on weighted
if weighted >= 90 and weighted <= 100:
    print('The weighted grade for', name,'is' ,'{:.1f}'.format(weighted))
    print(name, 'has a letter grade of ',grade)
elif weighted >= 80 and weighted <= 89:
    grade = 'B'
    print('The weighted grade for', name, 'is' ,'{:.1f}'.format(weighted))
    print(name, 'has a letter grade of ',grade)
elif weighted >= 70 and weighted <= 79:
    grade = 'C'
    print('The weighted grade for', name,'is' ,'{:.1f}'.format(weighted))
    print(name, 'has a letter grade of ',grade)
elif weighted >= 60 and weighted <= 69:
    grade = 'D'
    print('The weighted grade for', name,'is' , '{:.1f}'.format(weighted))
    print(name, 'has a letter grade of ',grade)
else:
    grade = 'F'
    print('The weighted grade for', name,'is' ,'{:.1f}'.format(weighted))
    print(name, 'has a letter grade of',grade)

print()
print('**** Thanks for using the Lab grade calculator ****')
        
