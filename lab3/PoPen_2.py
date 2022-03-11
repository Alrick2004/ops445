#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

import os
ls_return = os.popen('ls')
print('The contents of ls_return:',ls_return)
whoami_return = os.popen('whoami')
print('The contents of whoami_return:',whoami_return)
ifconfig_return = os.popen('ifconfig')
print('The contents of ifconfig_return:',ifconfig_return)