#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

# Place my_list below this comment (before the function definitions)
my_list = [1,2,3,4,5]

def add_item_to_list(ordered_list):
    ordered_list.append(max(ordered_list) + 1)
    return
    # Appends new item to end of list with the value (last item + 1)

def remove_items_from_list(ordered_list, items_to_remove):
        for i in range(len(items_to_remove)):
            if items_to_remove[i] in ordered_list:
                ordered_list.remove(items_to_remove[i])
    # Removes all values, found in items_to_remove list, from ordered_list

# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)