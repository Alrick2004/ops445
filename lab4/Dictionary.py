#!/usr/bin/env python3

# return_text_value() function
# Author ID: ahscott

#Begin by creating a new dictionary in a temporary Python file:
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Postal Code': 'M3J3M6', 'Province': 'ON'}

#All the values in a dictionary can be retrieved by using the dictionary.values() function. This particular function provides a list containing all values:
print(dict_york.values())

#We can retrieve individual values from a dictionary by providing the key associated with the value:
print(dict_york['Address'])
print(dict_york['Postal Code'])

#Dictionary keys can be any immutable values (i.e. not permitted for value to be changed). Types of values include: strings, numbers, and tuples.
dict_york['Country'] = 'Canada'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

#Let's change the province value to BC:
dict_york['Province'] = 'BC'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

#WARNING: Dictionary keys must be unique. Attempting to add a key that already exists in the dictionary will overwrite the existing value for that key! For example:
dict_york['Province'] = 'ON'
print(dict_york)
print(dict_york.values())
print(dict_york.keys())

#The lists that contain the values and keys of the dictionary are not real python lists - they are "views of the dictionary" and therefore are immutable. 
#You could change these views into usable lists by using the list() function:
list_of_keys = list(dict_york.keys())
print(list_of_keys[0])

#Lists can be used with for loops:
list_of_keys = list(dict_york.keys())
for key in list_of_keys:
    print(key)
for value in dict_york.values():
    print(value)