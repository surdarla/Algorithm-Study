# https://www.hackerrank.com/challenges/flipping-the-matrix/problem?isFullScreen=true

import math
import os
import random
import re
import sys


def flippingMatrix(matrix):
    
    n = len(matrix) // 2
    max_val = 0
    
    for i in range(n):
        for j in range(n):
            max_val += max(matrix[i][j], matrix[i][2*n-j-1], matrix[2*n-i-1][j], matrix[2*n-i-1][2*n-j-1])
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
