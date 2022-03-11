#!/usr/bin/env python3
'''Lab 3 Part 1 Function Receiving Multiple Arguments'''
# Author ID: ahscott 

def operate(number1, number2, operator):
 if operator == "add":
    number3 = number1 + number2
 elif operator == "subtract":
    number3 = number1 - number2
 elif operator == "multiply":
    number3 = number1 * number2
 else:
    return('Error: function operator can be "add", "subtract", or "multiply"')
 if 'number3' in locals():
    return(number3)
if __name__ == '__main__':
 print(operate(10, 5, 'add'))
 print(operate(10, 5, 'subtract'))
 print(operate(10, 5, 'multiply'))
 print(operate(10, 5, 'divide')) 