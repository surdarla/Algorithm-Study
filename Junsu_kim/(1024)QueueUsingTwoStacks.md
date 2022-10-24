# [Queue using two stacks](https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks)

## problem

In this challenge, you must first implement a queue using two stacks. Then process  queries, where each query is one of the following  types:

    1 x: Enqueue element  into the end of the queue.
    2: Dequeue the element at the front of the queue.
    3: Print the element at the front of the queue.

## code

```python
# with deque
from collections import deque
result = deque()
for i in range(int(input())):
    temp = list(map(int,input().split()))
    if temp[0] == 1:
        result.append(temp[1])
    elif temp[0] == 2:
        result.popleft()
    else:
        print(result[0])
```

```python
# with two stacks

```

## solve point

1. hackerrank에서 보기드문 input도 해줘야하는 문제
    - `map`함수 사용에서 list로 묶어서 담아줘야지 index를 사용할 수 있다는 check
2. deque를 사용해서 append popleft를 사용할 것
3. 제목에서처럼 two stack을 사용해서 푸는 것도 해볼 것
