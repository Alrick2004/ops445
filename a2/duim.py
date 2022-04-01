#!/usr/bin/env python                                           
# Author ID: ahscott

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
    parser.add_argument("-l", "--length", type=int, default=20, help="Specify the length of the graph. Default is 20.")
    # add argument for "human-readable". USE -H, don't use -h! -h is reserved for --help which is created automatically.
    # check the docs for an argparse option to store this as a boolean.
    # add argument for "target". set number of args to 1.
    args = parser.parse_args()


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
    pass


if __name__ == "__main__":
    pass


