#!/usr/bin/env python3
import os
import sys
'''
OPS445 Assignment 1 - Winter 2022

Program: assign1.py
Author: "Alrick Scott" - "064-306-111"

The python code in this file (assign1.py) is original work written by
"Alrick Scott". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: A program to display the date of birth entered in a specific format

Date: 2022-03-07
'''

def usage():
    "Returning the usage string to be displayed on the console as it is to inform the user about the valid inputs"
    return "Usage: a1_ahscott.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
    return "Usage: a1_ahscott.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD"
def leap_year(year):
    '''if it is divisible by 100 as well as  400 then its a leap year'''
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    #if it is not divisible by 100, but if it is divided by 4 it is a leap year    
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    else:
        return False


def sanitize(obj1,obj2):
    '''
    looping through each character in obj1 and if they are present in obj2, appending them to a new string and returing it
    '''
    date_str = ''
    for i in obj1:
        if i in obj2:
           date_str += i
    return date_str

def size_check(obj, intobj):
    '''
    to check obj is of the same length as intobj
    '''

    return len(obj) == intobj

def range_check(obj1, obj2):
    '''
    to check if obj is within the range of the two entries in obj2
    '''
    return obj1 >= obj2[0] and obj1 <= obj2[1]

        

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print(usage())
        sys.exit()
    
    month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    user_raw_data = sys.argv[1]
    allow_chars = '0123456789'
    dob = sanitize(user_raw_data, allow_chars)
   # setp 4
    result = size_check(dob,8)
    if result == False:
       print("Error 09: wrong date entered")
       sys.exit()
    # step 5
    year = int(dob[0:4])
    month = int(dob[4:6])
    day = int(dob[6:])
    # step 6
    result = range_check(year,(1900,9999))

    if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
    result = range_check(month,(1,12))
    if result == False:
       print("Error 02: wrong month entered")
       sys.exit()
    result = leap_year(year)
    if result == True:
       days_in_month[2] = 29
    result = range_check(day, (1, days_in_month[month]))
    if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
    # step 7
    new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
    # step 8
    print(new_dob)  

