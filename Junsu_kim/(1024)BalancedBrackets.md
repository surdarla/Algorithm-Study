# [Balanced Brackets - Queue](https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets)

## 1. Problem

By this logic, we say a sequence of brackets is balanced if the following conditions are met:

- It contains no unmatched brackets.
- The subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets.
- Given  strings of brackets, determine whether each sequence of brackets is balanced. If a string is balanced, return YES. Otherwise, return NO.

## 2. Code

```python
left = ['{','[','(']
right = ['}',']',')']
def isBalanced(s):
    temp = []
    if s[0] in right:
        return 'NO'
    for i in range(len(s)):
        now = s[i]
        if now in left:
            temp.append(left.index(now))
        else:
            if len(temp) == 0:
                return 'NO'
            pre = temp.pop()
            if right.index(now) != pre:
                return 'NO'
            pass
    if len(temp) == 0:
        return 'YES'
    else: return 'NO'
```

## solve point

- 기본적인 idea는 list에 left를 한쪽씩 차례로 넣어주고 right가 나올때마다 비교하는 것
- 같은 것 끼리 index를 사용해서 비교해주는 아이디어
- 그런데 예외사항이 몇 가지 있는 것을 잘 처리해 주어야 한다.
    1. 처음부터 right로 시작하는 경우 `}])`
    2. left만 나와서 temp에 쌓여서 끝나는 경우 `{[(`
    3. `{[}]`처럼 unbalanced한 경우는 바로 return
