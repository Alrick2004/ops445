#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

import os

ifconfig_return = os.popen('ifconfig')
ifconfig_contents = ifconfig_return.read()
print('The contents of ifconfig_return:', ifconfig_contents)