import math
import os
import random
import re
import sys

# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.

# 점대칭성. 뒤집기에 제한이 없으므로 점대칭하는 4개의 수중 최댓값만 골라서 더해주면된다.
def flippingMatrix(matrix):
    # Write your code here
    lenth = len(matrix[0])
    half = lenth//2
    
    # point symmetry 
    q_sum = 0
    for i in range(half):
        for j in range(half):
            q_sum += max(matrix[i][j], matrix[i][lenth-j-1], matrix[lenth-i-1][j], matrix[lenth-i-1][lenth-j-1]) 
    return q_sum