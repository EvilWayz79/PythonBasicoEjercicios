import math
import os
import random
import re
import sys

def miniMaxSum(arr):
        
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(0, n-i-1):    
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
    if not swapped:
        pass
    
    minSum = sum(arr[:4])
    maxSum = sum(arr[1:])
    
    
    print(f'{minSum}{"\u0020"*2}{maxSum}')
                



if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))
    
    miniMaxSum(arr)
    
    