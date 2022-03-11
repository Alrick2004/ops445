#!/usr/bin/env python3

# Python Script Demonstrating Handling Exceptions
# Author ID: ahscott

def read_file_string(fileName):
    f = open(fileName,'r') #opens the file to read
    return f.read() # return its entire contents as string
    f.close()
    
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

def append_file_string(file_name,string_of_lines):
    f = open(file_name,'a') #opens the file in append mode
    f.write(string_of_lines) # appends the string of lines to the file
    f.close()


def write_file_list(file_name,list_of_lines):
    f = open(file_name,'w') #opens the file in write mode
    for line in list_of_lines:# loops through the list of lines
        f.write(line + '\n') # write each line into the file with a newline at the end
    f.close()

def copy_file_add_line_numbers(file_name_read,file_name_write):
    f1 = open(file_name_read,'r')
    f2 = open(file_name_write,'w')
    lines = f1.readlines() # reading the file contents as list of lines
    for i in range(0,len(lines)): # looping from 0 till the length of the lines list
        f2.write(str(i + 1) + ":" + lines[i]) # writing each line with the line number
    f1.close()
    f2.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string_of_lines = "First Line\nSecond Line\nThird Line\n"
    list1 = ["Line 1","Line 2","Line 3"]
    append_file_string(file1,string_of_lines)
    print(read_file_string(file1))
    write_file_list(file2,list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2,file3)
    print(read_file_string(file3))
