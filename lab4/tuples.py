#!/usr/bin/env python3

# return_text_value() function
# Author ID: ahscott

t1 = ('Prime', 'Ix', 'Secundus', 'Caladan')
t2 = (1, 2, 3, 4, 5, 6)
print(t1[0])
print(t2[2:4])

print('Ix' in t1)
print('Geidi' in t1)

list2 = [ 'uli101', 'ops235', 'ops335', 'ops445', 'ops535', 'ops635' ]
list2[0]= 'ica100'
print(list2[0])
print(list2)

#If you would like a tuple with an item different from the tuple you currently have, then you must create a new one.
#t2[1] = 10  #Once created an item in a tuple can not be changed.

#The following creates a new tuple (t3) with a contents from a slice of the t2 tuple. Slicing works the same way for tuples as for lists:
t3 = t2[2:3]
print(t3)

for item in t1:
    print('item: ' + item)