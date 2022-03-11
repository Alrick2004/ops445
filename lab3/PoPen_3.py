#!/usr/bin/env python3
'''PART 2 - Launching Linux command and controlling its process with builtin functions in os and subprocess modules'''
# Author ID: ahscott 

import os
whoami_return=os.popen('whoami')
whoami_contents = whoami_return.read()
print('whoami_contents:',whoami_contents)