#!/usr/bin/env python3

# Python Script Demonstrating Writing to Files
# Author ID: ahscott

def read_file_string(file_name):
    f = open(file_name,'r') #opens the file to read
    list1 =  f.read() # return its entire contents as string
    f.close()
    return list1
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    f = open(file_name,'r') #opens the file to read
    lines =  f.readlines()
    output = []
    for line in lines:
        output.append(line.strip('\n')) # return its entire contents and splits them to parts whenever it sees newline character
    f.close()
    return output
    # Takes a file_name as string for a file name and
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))