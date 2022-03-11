#!/usr/bin/env python3
'''PART 2 - Manipulating Items in Lists'''
# Author ID: ahscott 

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
length_of_list = len(list_of_numbers)    # Returns the length of the list
smallest_in_list = min(list_of_numbers)  # Returns the smallest value in the list
largest_in_list = max(list_of_numbers)   # Returns the largest value in the list

# Notice how the long line below is wrapped to fit on one screen:
print("List length is " + str(length_of_list) + 
      ", smallest element in the list is " + str(smallest_in_list) +
      ", largest element in the list is " + str(largest_in_list))

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
for item in list_of_numbers:
    print(item)

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]

def square(num):
    return num * num

for value in list_of_numbers:
    print(square(value))

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]

# Squares each item in a list of numbers, returns new list with squared numbers
def square_list(number_list):
    new_list = []
    for number in number_list:
        new_list.append(number * number)
    return new_list

new_list_of_numbers = square_list(list_of_numbers)
print(list_of_numbers)
print(new_list_of_numbers)

list_of_numbers = [ 1, 5, 2, 6, 8, 5, 10, 2 ]
def delete_numbers(numbers):
    numbers.remove(5)
    numbers.remove(6)
    numbers.remove(8)
    numbers.remove(5)
delete_numbers(list_of_numbers)
print(list_of_numbers)