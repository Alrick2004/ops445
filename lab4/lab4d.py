#!/usr/bin/env python3

# Create a Python Script Demostrating Substrings
# Author ID: ahscott

str1 = "Hello World!!"
str2 = "Seneca College"

num1 = 1500
num2 = 1.50

def first_five(str1):
    return str1[0:5]

def last_seven(str1):
    return str1[len(str1) - 7:]
def middle_number(num):
    return str(num)[1] + str(num)[2]

def first_three_last_three(str1,str2):
    return str1[0:3] + str2[len(str2) - 3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1,str2))
    print(first_three_last_three(str2,str1))
    
