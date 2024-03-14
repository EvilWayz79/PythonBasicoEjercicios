#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#  12:00:00PM

def timeConversion(s):
    # Write your code here
    elements = s.split(':')
    
    hh = elements[0]
    mm = elements[1]
    ss = elements[2][:2]
    disc = elements[2][2:]
    
    if hh == '12' and disc == 'AM':
        hh = '00'
    elif disc == 'PM' and hh != '12':
        hh = int(hh)
        hh += 12
    
    print(f'{hh}:{mm}:{ss}')
        
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    #fptr.write(result + '\n')

    #fptr.close()
