# https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

import math
import os
import random
import re
import sys

def minimumBribes(q):
    bribe_num = 0
    for i in range(len(q)-1,0,-1):
        if q[i] != (i+1) :
            if q[i-1] == (i+1) :
                bribe_num += 1
                q[i-1], q[i] = q[i], q[i-1]

            elif q[i-2] == (i+1) :
                bribe_num += 2
                q[i-2], q[i-1] = q[i-1], q[i-2]
                q[i-1] , q[i] = q[i], q[i-1]

            else:
                bribe_num = "Too chaotic"
                break

    print(bribe_num)

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
