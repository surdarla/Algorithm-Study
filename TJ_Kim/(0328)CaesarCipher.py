#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#
# maketrans(), translate() method 활용으로 쉽게 해결. 코드를 더 줄일 수 있을거 같긴한데, 이대로도 문제 없을듯 ?

def caesarCipher(s, k):
    # Write your code here
    k %= 26  # test case 에서 k 값이 26을 넘어가면 문제 발생. 26 으로 나눈 나머지로 ㄱㄱ
    small = 'abcdefghijklmnopqrstuvwxyz'
    big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    intab = small
    outtab = intab[k:]+intab[:k]
    intab2 = big
    outtab2 = intab2[k:]+intab2[:k]
    
    transtab = s.maketrans(intab, outtab)
    transtab2 = s.maketrans(intab2, outtab2)
    
    s = s.translate(transtab2)
    return s.translate(transtab)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()