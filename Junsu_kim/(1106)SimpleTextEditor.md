# [Simple Text Editor](https://www.hackerrank.com/challenges/one-week-preparation-kit-simple-text-editor)

## problem

    차례로 주어지는 type과 rest operation에 따라
    순서대로 '' 빈 string을 고쳐가는 코드 완성하기

## code

```python
# denoting the # of operations
s = ''
q = int(input())
stor = []

for i in range(q):
    op = input().split()

    if int(op[0]) == 1: # append, stor
        s+=op[1]
        stor.append(s)
    elif int(op[0]) == 2: # delete, stor
        s = s[:-(int(op[1]))]
        stor.append(s)
    elif int(op[0]) == 3: # print, no stor
        print(s[int(op[1])-1])
    else: # undo
        stor.pop() # present s out
        if stor:
            s = stor[-1]
        else:
            s = '' # if stor is empty -> undo goes to base s which is ''(empty string)
```

## solve point

1. undo를 처리하는 것이 중요. undo가 2번이상 연달아 나오는 경우를 위해서 따로 def로 만드는 것보다는 for문안에 달아서 하는 것이 효과적으로 보이며, dp처럼 `저장을 해놨다가 가져가는 것`이 효율적으로 보였음
2. op[1] 부분이 1의 경우를 제외하고는 Index를 받아오는 int로 사용되기 때문에 주의가 필요함.
3. stor가 비어있지 않았는가의 경우에 따라서 다르게 사용되어야 하기 때문에 `if stor`문으로 비어있지 않았나를 확인하는 것. stor에서 한번 먼저 pop을 해줌으로서 undo를 할수 있도록 해야한다.
4. `It is guaranteed that the sequence of operations given as input is possible to perform.`라고 했지만 마지막의 `if not stor -> s = ''`의 경우는 결국 시작의 s는 빈 문자열 `''`이기 떄문에 저렇게 처리했음.
