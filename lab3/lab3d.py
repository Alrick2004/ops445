#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

import subprocess

def free_space():
    free_space = subprocess.check_output( "df -h | grep '/$' | awk '{print $4}'", shell= True)
    p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output = p.communicate()
    stdout = free_space.decode('utf-8').strip()
    return stdout

if __name__ == '__main__':
    space = free_space()
    print(space)