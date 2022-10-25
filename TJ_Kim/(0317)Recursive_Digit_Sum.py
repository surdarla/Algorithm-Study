def sum_digit(n):
    while len(n) > 1:
        n = list(map(int, str(n).strip()))
        n = sum(n)
        n = str(n)
    else :
        return n

def superDigit(n, k):
    n = str(k * int(n))
    return sum_digit(n)
