#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

import os

ls_return = os.system('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.system('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.system('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)
ipconfig_return = os.system('ipconfig')
print('The contents of ipconfig_return:',ipconfig_return)