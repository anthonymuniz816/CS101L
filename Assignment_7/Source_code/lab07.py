#CS 101 Lab
#Program 7
#Name: Anthony Muniz
#Email: AMMW5@umsystem.edu

#PROBLEM: Need to develop a code that takes in a user input and then encodes or
#decodes the input depending on the user's selection.

#ALGORITHM:
#START
#Make function that asks the user for the minimum mpg
#If user inputs a number higher than 100 or lower than 0, it will ask again until correct input is inputted
#If user inputs number between 1-100, the funciton will return the input
#Make a function that asks the user to input the name of the file they want to access
#Input will be returned once the correct file name is inputted
#Make function that asks the user to input the name of the file they want to output to
#Make a function that combines all the previous functions in a way that will make the program work as a whole
#Call the last function in the main
#END

def minimum_mpg():
    while True:
        try:
            mpg= float(input('Enter the minimum mpg ==> '))
            if mpg<0:
                print('Fuel economy given must be greater than 0')
            elif mpg>100:
                print('Fuel economy given must be less than 100')
            else: 
                return mpg
        except ValueError:
            print('You must enter a number for the fuel economy')

def get_file():
    while True:
        file_name= input('Enter the name of the input vehicle file ==> ')
        try:
            with open(file_name, 'r') as read_file:
                return [[data.strip() for data in line.strip().split('\t')] for line in read_file.readlines()]
        except FileNotFoundError:
            print('Could not open file',file_name)
       

def write_to_file(mpg, file_data):
    while True:
        try:
            file_name= input('Enter the name of the file to output to ==> ')
            with open(file_name, 'w') as write_file:
                for data in file_data:
                    try:
                        if mpg >= float(data[7]):
                            write_file.write['(0:<5)(0:<20)(1:<40)(3:>10)\n'.format(data[0],data[1],data[2],data[7])]
                    except:
                        print('Could not convert value invalid for vehicle',data[0],data[1],data[2])
        except IOError:
            print('There is an IO Error',file_name)
        

def main():
    min_mileage=minimum_mpg()
    file_data=get_file()[1:]
    write_to_file(minimum_mpg(), file_data)

main()


