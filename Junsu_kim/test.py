# from collections import deque

# n,limit = map(int,input().split())
# result = 0
# record = []
# for _ in range(n):
#     w,v = map(int,input().split())
#     if not w>limit:
#         record.append([w,v,v/w])

# record = deque(sorted(record,key=lambda x:x[2],reverse=True))

# while len(record)>1:

#     now = record.popleft()
#     left = limit - now[0]
#     this_max = now[1]
#     for i in record:
#         if left == 0:
#             break
#         if i[0] <= left:
#             left -= i[0]
#             this_max += i[1]

#     if this_max > result:
#         result = this_max


# print(result)

stuff = [[0,0]]
n,k = map(int,input().split())
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
    stuff.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,k+1):
        w = stuff[i][0]
        v = stuff[i][1]

        if j < w:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(
                v+knapsack[i-1][j-w],
                knapsack[i-1][j]
                )

print(knapsack[n][k])
