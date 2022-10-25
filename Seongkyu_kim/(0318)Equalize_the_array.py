import math
import os
import random
import re
import sys

# 1안
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

# 2안
import numpy as np
def equalizeArray(n, arr):
		value, counts = np.unique(arr, return_counts=True)
		return n-max(counts)

if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(n, arr)

    print(f'result : {result}')
