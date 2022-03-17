import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def equalizeArray(n, arr):
    unique_list = []
    count_list = []
    arr.sort()
    # Write your code here
    for num in arr:
        if num not in unique_list:
            unique_list.append(num)
            count_list.append(1)
        else:
            count_list[-1] += 1
    result = max(count_list)
    return n-result

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    
    result = equalizeArray(n, arr)

    print(f'result : {result}')
