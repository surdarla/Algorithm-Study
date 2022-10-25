# 1. [Lonely integer](https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two)

```python
# The function is expected to return an INTEGER
# The function accepts INTEGER_ARRAY a as parameter

from collections import Counter
def lonelyinteger(a,n):
    return Counter(a).most_common[n](-1)[0]
```

- n개의 unique 숫자들이 있다. arr를 카운터 해준뒤에 n만큼 most_common해주면 결국 가장 빈도가 적은  쌍을 return 해주고 이것의 key[0]를 return하면 1만큼만 등장한 녀석이 튀어나오게 된다.

# 2. [Diagonal Difference](https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen)

```python
# The function is expected to return an INTEGER
# The function accepts 2D_INTEGER_ARRAY arr as parameter


def diagonalDifference(arr,n):
    answer = 0
    step = 0
    for i in range(n):
        temp = arr[i][step] - arr[i][n-1-step]
        step += 1
        answer += temp
    return abs(answer)
```

- 행에서 끝과 끝을 빼주는 것들을 더하되, 행을 내려가면서 한칸씩 앞뒤로 한칸씩 땡기면 된다.
- 다 더해준뒤에 마지막에 abs 한번만 해줘야한다.

# 3. [Counting Sort 1](https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-two&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen)

```python
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def countingSort(arr):

    result = [0]*100
    for i in arr:
        result[i] += 1
    return result
```

- 100개 까지라는게 포인트.

## counting sort에 대한 고찰

> $n * log(n)$을 가지는 compariosn sorts(merge,quick,insert)들과 비교했을때 어떤 강점?

- [stackoverflow 비교](https://stackoverflow.com/questions/47736838/why-is-quick-sort-better-than-counting-sort)
  - 카운팅 소트가 $O(n)$의 시간복잡드롤 가지긴 하지만
  - *사실상 min - max의 사이 k값이 엄청나게 크거나* - 해당 경우에는 사실상 $O(n+k)$를 가진다.
  - *int가 아니라 string*에 대한 카운트를 해야할 경우는 quick이 좋다.
  - 하지만 범위상의 모든 경우를 0개가 나오는 것 까지 포함하는 배열을 만들어줄때는 좋은 대안이 될 수 있다.

- [lower Bound](https://www.cs.cmu.edu/~avrim/451f11/lectures/lect0913.pdf)
  - since  represents the minimum number of comparisons needed to know where to place each element.
  - 비교정렬 + 최악 = n log(n)을 초월할 수 없다는 이야기

### mockup test
[Flipping the Matrix - medium](https://www.hackerrank.com/challenges/flipping-the-matrix/problem?isFullScreen=true) 못풀음 다시풀어야함.
