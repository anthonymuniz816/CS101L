#Anthony Muniz
#Program 9
#CS 101 LAB

#Prolem:Need to develop a program that asks the user to input a csv file, then asks the user for the type of crime
#they specifically want to look at, and output such information.

#ALGORITHM:
#START
#Create function month_from_number
#Create function read_in_file
#Create function create_reported_date_dict
#Create function create_reported_month_dict
#Create function create_offense_dict
#Create function create_offense_by_zip
#MAIN
#Create while loop and set to True
#Create Try statement
#Ask user to input name of csv file
#Call functions previously created
#Print month with highest number of crimes
#Print offense with highest number of crimes
#Create another while loop in the try statement and set to True
#Ask user for the type of offense
#If input is valid, display information and end program
#If input is not valid, ask again
#Create an except statement for a file not found error
#If error occurs from step 3 in the MAIN, ask user again
#END

import csv

def month_from_number(num):
    months={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    return months[num]


def read_in_file(user_file):
    file = open(user_file, encoding='utf-8')
    csv_read = csv.reader(file)
    rows=[]
    for ln in csv_read:
        rows.append(ln)
    del rows[0]
    file.close()
    return rows

def create_reported_date_dict(user_list):
    dict_={}
    for i in user_list:
        if i[1] in dict_:
            dict_[i[1]] += 1
        else:
            dict_[i[1]] = 1
    return dict_

def create_reported_month_dict(user_list):
    dict_ = {} 
    for i in user_list:
        x = int(i[1][1])
        if x in dict_:
            dict_[x] += 1
        else:
            dict_[x] = 1
    return dict_

def create_offense_dict(user_list):
    dict_ = {} 
    for i in user_list:
        if i[7] in dict_:
            dict_[i[7]] += 1
        else:
            dict_[i[7]] = 1
    return dict_

def create_offense_by_zip(user_list):
    dict_ = {}
    for i in user_list:
        dict_2 = {}
        if i[7] not in dict_:
            for x in user_list:
                if x[7] == i[7]:
                    if x[13] in dict_2:
                        dict_2[x[13]] += 1
                    else:
                        dict_2[x[13]] = 1
                    dict_[i[7]] = dict_2
    return dict_
 

if __name__ == "__main__":

    while True:
        try:
            user_file= input('Enter the name of the crime data file ==> ')
            user_list = read_in_file(user_file)
            date = create_reported_date_dict(user_list)
            month = create_reported_month_dict(user_list)
            offense = create_offense_dict(user_list)
            offense_zip = create_offense_by_zip(user_list)
            month_list= sorted([[k,v] for k,v in month.items()])
            offense_list = sorted([[k,v] for k,v in offense.items()])
           
            print('The month with the highest # of crimes is {} with {} offenses'.format(month_from_number(month_list[-1][0]),max(month.values())))
            print('The offense with the highest # of crimes is {} with {} offenses'.format(offense_list[-1][0],max(offense.values())))
            print()
            while True:
                offense_option = input('Enter an offense ==> ')
                valid_offense = offense_zip.get(offense_option,'x')
                if valid_offense == 'x':
                    print('Not a valid offense found, please try again')
                    continue
                else:
                    break
            print()
            print(offense_option,'Offenses by Zip Code')
            print('{:<20}{:>5}'.format('Zip Code','# Offenses'))
            print('='*30)
            for k,v in offense_zip.items():
                if k == offense_option:
                    for k2,v2 in v.items():
                        print('{:<25}{:>5}'.format(k2, v2))
            break
        
        except FileNotFoundError:
            print('Could not find the specified file. {} not found.'.format(user_file))





