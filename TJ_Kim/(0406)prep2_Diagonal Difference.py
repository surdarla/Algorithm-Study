def diagonalDifference(arr):
    # Write your code here
    rightdown = 0
    leftdown = 0
    for i in range(n):
        leftdown += arr[i][i]
        rightdown += arr[i][-i-1]  #[i][-i-1] works same
    return abs(leftdown - rightdown)