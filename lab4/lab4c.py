#!/usr/bin/env python3

# Create a Python Script for Managing Dictionaries
# Author ID: ahscott

dict_york = {'Address':'70 The Pond Rd','City':'Toronto','Country':'Canada','Postal Code':'M3J3M6','Province':'ON'}
dict_newham = {'Address':'1750 Finch Ave E','City':'Toronto','Country':'Canada',
               'Postal Code':'M2J2X5','Province':'ON'}

list_keys = ['Address','City','Country','Postal Code','Province']
list_values = ['1750 Finch Ave E','Toronto','Canada','M2J2X5','ON']

def create_dictionary(keys,values):
    dict = {}
    for i in range(0,len(list_keys)):
        dict[keys[i]] = values[i]
    return dict
def shared_values(dict1,dict2):
    list1 = []
    for value1 in dict1.values():
        for value2 in dict2.values():
            if value1 == value2:
                list1.append(value1)
    return set(list1)
        

if __name__ == '__main__':
    york = create_dictionary(list_keys,list_values)
    print("York: ",york)
    common = shared_values(dict_york,dict_newham)
    print("Common: ",common)
