# [New year chaos - Constructive Algorithm](https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four)

## codes

### solve 1

```python
# Complete the 'minimumBribes' function below.
# The function accepts INTEGER_ARRAY q as parameter.
def minimumBribes(q):
    moves = 0 
    q = [x-1 for x in q] #index랑 숫자 맞추기
    for i,P in enumerate(q):
        if P - i > 2: #자릿수 차이가 3이상
            print("Too chaotic")
            return
        
        for j in range(max(P-1,0),i): #max는 0이하의 index에 대한 탐색을 방지하는 것.
            if q[j] > P:
                moves += 1
    print(moves)
```
