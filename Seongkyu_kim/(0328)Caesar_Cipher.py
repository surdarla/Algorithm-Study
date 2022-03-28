# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three

import math
import os
import random
import re
import sys

def caesarCipher(s, k):
    # Write your code here
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet_lower.upper()
    new_k = k % len(alphabet_lower)
    alphabet_lower_changed = alphabet_lower[new_k:] + alphabet_lower[:new_k]
    alphabet_upper_changed = alphabet_upper[new_k:] + alphabet_upper[:new_k]

    my_sentence = ''

    for char in s:
        if char in alphabet_lower:
            original_index = alphabet_lower.index(char)
            my_sentence += alphabet_lower_changed[original_index]
        elif char in alphabet_upper:
            original_index = alphabet_upper.index(char)
            my_sentence += alphabet_upper_changed[original_index]
        else:
            my_sentence += char
    return my_sentence


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()