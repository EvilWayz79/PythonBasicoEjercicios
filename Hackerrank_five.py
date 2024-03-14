#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # for easy input
    #a = [1, 2, 3, 4, 3, 2, 1]
    #a = [1, 2, 3, 1, 3, 2, 9]
    #a = [4, 5, 6, 7, 6, 5, 4]
    a = [4, 5, 6, 5, 6, 3, 4]
    # Write your code here
    
    returnInt = -1
    
    for i in  range(len(a)):
        found = False
        for j in range(math.ceil(len(a)/2) ):
            if a[i] == a[j] and i != j:
                found = True
                break
        for k in range(len(a) - 1, math.ceil(len(a)/2) - 1, -1):
            if a[i] == a[k] and i != k:
                found = True
                break
        
        if not found:
            returnInt = a[i]
            break
        
    return returnInt
        
            
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    
    print(result)

    #fptr.write(str(result) + '\n')

    #fptr.close()