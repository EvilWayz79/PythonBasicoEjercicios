#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arrLength = len(arr)
    pos = neg = zero = 0
    for i in range(arrLength):
        if arr[i] > 0 :
            pos +=1
        elif arr[i] < 0 :
            neg += 1
        else:
            zero += 1
    print(f'{pos/arrLength :.6f}')
    print(f'{neg/arrLength :.6f}')
    print(f'{zero/arrLength :.6f}')     
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

