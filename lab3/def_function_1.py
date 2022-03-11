#!/usr/bin/env python3
#PART 1 - Function that does not take argument or return value
def hello():
    print('Hello World')
    print('Inside a Function')
    return

my_stuff = hello()
print('Stuff return from hello():',my_stuff)
print('the object my_stuff is of type:',type(my_stuff))