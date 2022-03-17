# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k

def superDigit(n, k):

    temp = str(k * sum([int(x) for x in n]))
    return myfunc(temp)

def myfunc(n):
    if len(n) == 1:
        return int(n)
    else:
        temp = str(sum([int(x) for x in n]))
        return myfunc(temp)
    