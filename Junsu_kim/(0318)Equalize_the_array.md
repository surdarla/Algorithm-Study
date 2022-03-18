```python

# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def equalizeArray(arr):
    from collections import Counter
    c = Counter(arr)
    max_count = c.most_common(1)[0][1]
    return sum(c.values()) - max_count
```

## collections - Counter

![collections](/Junsu_kim/img/collections.png){: width="100" height="100"}

- {element : count_num , ...} 형식으로 쉽게 카운팅 가능
- 완전히 제거하려면 del 함수를 사용해야함.

### methods

- elements() : 개수만큼 반복되는 요소에 대한 이터레이터를 반환
- most_common[n] : 가장 빈도수 높은 순으로 n개의 튜플을 리스트로 반환
- subtract[iterable-or-mapping] : c.subtract(d) 이런식으로 카운팅끼리의 빼기
- total() == sum(Counter(?).values())

```python
c.total()                       # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
```
