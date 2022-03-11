#!/usr/bin/env python3

#Author: Alrick Scott
#Author ID: ahscott
#Date Created: 2022-01-22

import sys
if (len(sys.argv) == 2):
    timer = int(sys.argv[1])
else:
    timer = 3
while timer > 0:
    print(timer)
    timer = timer - 1
print("blast off!")


