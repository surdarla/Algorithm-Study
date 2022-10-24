# [Pairs](https://www.hackerrank.com/challenges/pairs)

## 1. problem

Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

## 2. code

```python
# with deque - fail in 5 tests for time limit exceeded
from collections import deque
def pairs(k, arr):
    s = deque(sorted(arr))
    result = 0
    for i in range(len(s)):
        now = s.popleft() + k
        if now in s:
            result += 1
    return result
```

[check - two pointer solution](https://medium.com/@xww0701/hackerrank-pairs-python-solution-20fb4ef6321d)

```python
# two pointer
def pairs(k, arr):
    result = 0
    arr = sorted(arr)
    j = 1
    for i in range(len(arr)-1):
        while j<len(arr):
            if arr[j] - arr[i] == k:
                result += 1
                j += 1
            elif arr[j] - arr[i] > k:
                break
            elif arr[j] - arr[i] < k:
                j += 1
    return result
```

## 3. solve point

- deque로 sorted한 뒤에 앞에서 popleft로 뽑아내면서 뒤로 비교해가는 방향을 사용했었는데 5가지 경우에서 time limit exceeded 판정이 나서 정답지를 찾아보았다.
- two pointer를 사용하는 경우에 아주 빠르게 문제를 푸는 것을 보고 충격을 받았다.
    1. deque로 popleft를 해주는게 아니라 while문의 j를 +=1 해주면서 pointer로 사용하면서 비교해나간다.
    2. 리스트를 수정할 필요가 없다.
