#!/usr/bin/env python3

# return_text_value() function
# Author ID: ahscott

s1 = {'Prime', 'Ix', 'Secundus', 'Caladan'}
s2 = {1, 2, 3, 4, 5}
s3 = {4, 5, 6, 7, 8}

#Try to access a set through the index:
#print(s1[0])
#This should have caused an error. You cannot access data inside a set this way because the elements inside are unordered. Instead, you should use the in operator to check to see whether a value is contained in the set:

#Sets can be combined, but it is important to note that any duplicate values (shared among sets) will be deleted.
print('Ix' in s1)
print('Geidi' in s1)

#This is how you get a set containing only UNIQUE values (no duplicates) from both sets:
print(s2 | s3)         # returns a set containing all values from both sets
print(s2.union(s3))    # same as s2 | s3

#Instead of combining sets, we can display values that are common to both sets. This is known in mathematical terms as an intersection between the lists:
print(s2 & s3)             # returns a set containing all values that s2 and s3 share
print(s2.intersection(s3)) # same as s2 & s3

#Sets can also have their values compared against other sets. First find out what items are in s2 but not in s3. This is also called a difference:
print(s2)
print(s3)
print(s2 - s3)             # returns a set containing all values in s2 that are not found in s3
print(s2.difference(s3))   # same as s2 - s3

#In order to see every difference between both sets. 
# You need to find the symmetric difference. This will return a set that shows all numbers that both sets do not share together:
print(s2 ^ s3)                     # returns a set containing all values that both sets DO NOT share
print(s2.symmetric_difference(s3)) # same as s2 ^ s3

#Note: the set() function can convert lists into sets, and the list() function can convert sets into lists. The operations in this section can only be applied to sets, so if you need to perform a union, intersection, or difference between lists, you need to convert them to sets first. 
# For example:
l2 = [1, 2, 3, 4, 5]
l3 = [4, 5, 6, 7, 8]
temporary_set = set(l2).intersection(set(l3))
new_list = list(temporary_set)  # '''set()''' can make lists into sets. '''list()''' can make sets into lists.
print(new_list)