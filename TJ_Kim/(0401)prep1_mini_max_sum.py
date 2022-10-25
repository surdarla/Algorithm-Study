def miniMaxSum(arr):
    # Write your code here
    sum_ = sum(arr)
    min_ = min(arr)
    max_ = max(arr)
    print(sum_ - max_, sum_ - min_)
