#!/usr/bin/env python3
# Student ID: ahscott

import subprocess, sys
import os
import argparse



'''
OPS445 Assignment 2 - Winter 2022
Program: duim.py 
Author: Alrick Scott
The python code in this file (duim.py) is original work written by
Alrick Scott. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

Description: <Enter your documentation here>

Date: 
'''

def parse_command_args():
    "Set up argparse here. Call this function inside main."
    parser = argparse.ArgumentParser(description="DU Improved -- See Disk Usage Report with bar charts",epilog="Copyright 2022")
    parser.add_argument("-H","--human-readable",action="store_true",help="print sizes in human readable format (e.g. 1K 23M 2G)")
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    parser.add_argument('directory', metavar='target', type=ascii, nargs=1,
                    help='The directory to scan.')
    
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    args = parser.parse_args()
    return args


def percent_to_graph(percent, total_chars):
    "returns a string: eg. '##  ' for 50 if total_chars == 4"
    if percent < 0 or percent > 100:
        print("Invalid percent value")
        return
    else:
        #Will use equal signs to denote the percentage, so naming the variables matching that
        equals = int((percent/100) * total_chars)
        equal_chars = ''
        space_chars = ''
        for i in range(0,equals):
            equal_chars += "="
        for i in range(0,(total_chars - equals)):
            space_chars += ' '
        return equal_chars + space_chars

def call_du_sub(location):
    "takes the target directory as an argument and returns a list of strings"
    "returned by the command `du -d 1 location`"
    process = subprocess.Popen('du -d 1 ' + location,stdout=subprocess.PIPE,stdin =       subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    output = process.communicate()
    return list(output)

def create_dir_dict(alist):
    "gets a list from call_du_sub, returns a dictionary which should have full"
    "directory name as key, and the number of bytes in the directory as the value."
    dic = {}
    arr1 = alist[0].decode('utf-8').strip().split('\n')
    for i in arr1:
       arr2 = i.split('\t')
       if len(arr2) > 1: 
       	 dic[arr2[1]] = arr2[0]		
    return(dic)
    	


if __name__ == "__main__":
    parse_command_args()

    if len(sys.argv) > 1 :
      print("You cannot enter more than 2 arguments")
      sys.exit(-1)
    elif len(sys.argv) < 2:
      alist = call_du_sub('./')
    else:
      alist = call_du_sub(sys.argv[1])
    new_dict = create_dir_dict(alist)
    total_size = 0.0
    for key,value in new_dict.items():
        
        total_size += float(value[0:len(value) - 1])
    
    for key,value in new_dict.items():
        if key != sys.argv[1]:
            value = float(value[0:len(value) - 1])
            print(str((value/total_size)*100) +" "+ percent_to_graph(value/total_size,10) + " " + key)    
