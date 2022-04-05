def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter
            

def lonelyinteger(a):
    # Write your code here
    for i, j in countLetters(a).items():
        if j == 1:
            return i