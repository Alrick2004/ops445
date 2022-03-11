#!/usr/bin/env python3
#PART 2 - Function that does not take argument but returns a string
def return_text_value():
    name = 'Terry'
    greeting = 'Good Morning ' + name 
    return greeting
text = return_text_value()
print(text)