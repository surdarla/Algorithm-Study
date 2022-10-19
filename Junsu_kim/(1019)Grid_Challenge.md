# [Grid Challenge](https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge)

## 1. problem

    Determine if the columns are also in ascending alphabetical order, top to bottom. Return YES if they are or NO if they are not.

## 2. codes

```python
def gridChallenge(grid):
    min_ord_list,max_ord_list = [],[]
    for i in grid:
        max_ord_list.append(max_ascii_inlist(i))
        min_ord_list.append(min_ascii_inlist(i))
    if sorted(max_ord_list) == max_ord_list and sorted(min_ord_list)==min_ord_list:
        return 'YES'
    return 'NO'

def max_ascii_inlist(li):
    m = 0
    for i in li:
        now = ord(i)
        if now > m:
            m = now
    return m

def min_ascii_inlist(li):
    m = 1000000
    for i in li:
        now = ord(i)
        if now < m:
            m = now
    return m
```

## 3. solve point

주어지는 row들을 알파벳 순서대로 배열하여 column적으로도 정렬이 가능한지를 묻는 문제이다. 알파벳을 ascii로 변경하면 편하게 정수로 대수비교가 가능하다.\
다만 row 별로 최댓값만 비교하면 틀리게 된다. min값도 비교를 해줘야한다. 그렇지 않으면 row안에서는 정렬이 될지라고 column 전체적으로보면 위에 행에서 더 큰 값이 있을 수 있기에 NO가 나와야하는 것에 반응하지 못한다.
