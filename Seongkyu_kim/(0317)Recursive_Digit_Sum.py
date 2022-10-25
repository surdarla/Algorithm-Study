
# https://www.hackerrank.com/challenges/recursive-digit-sum/problem?isFullScreen=true

import math
import os
import random
import re
import sys

def superDigit(n, k, Flag):
    # Write your code here
    if Flag:
        new_n = str(n)
        sum_number = 0
        for i in new_n:
            sum_number += int(i)
        new_n = str(sum_number)*k
        Flag = False
    else:
        new_n = str(n)

    if len(new_n) < 2:
        return int(new_n)
    else:
        sum_number = 0
        for i in new_n:
            sum_number += int(i)
    return superDigit(sum_number, k, Flag)

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    Flag = True
    result = superDigit(n, k, Flag)

    print(f'result : {result}')
