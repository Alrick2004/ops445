#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

import os
import subprocess
p = subprocess.Popen(['date'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

output = p.communicate()
print(output)
print(output[0])
# The above stdout is stored in bytes
# Convert stdout to a string and strip off the newline characters
stdout = output[0].decode('utf-8').strip()
print(stdout)