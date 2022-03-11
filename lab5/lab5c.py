#!/usr/bin/env python3

# Python Script Which Handles Errors
# Author ID: ahscott

def add(number1,number2):
    try:
        sum = int(number1) + int(number2)# add the two numbers passed,even if they are in string format and storing it in sum 
        return sum #returns the sum
    except ValueError:# this error occurs if any number passed contains anything other than digits
        return 'error: could not add numbers'
def read_file(filename):
    
    try:
        f = open(filename,'r')
        output =  f.readlines() # returns a list of all lines
        f.close()
        return output
    except FileNotFoundError: # This error occurs if the file cannot be found in the system
        return 'error: could not read file'
    
    

if __name__ == '__main__':
    print(add(10,5))
    print(add('10',5))
    print(add('abc',5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))
