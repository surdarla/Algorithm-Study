from collections import Counter

def equalizeArray(arr):
    return sum(Counter(arr).values()) - max(Counter(arr).values())

