# preparation kit 4

## [Grid Challenge](https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four)

```python
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):

    for i in range(len(grid[0])):
        col = []
        for j in range(len(grid)):
           col.append(grid[j][i])
           if col != sorted(col):
            return 'NO'
    return 'YES'
```

- 안풀림. test case 2개만 맞고 나머지는 틀림
- 나중에 다시 풀어보기

## [Truck Tour](https://www.hackerrank.com/challenges/truck-tour/problem?h_r=internal-search&isFullScreen=true)

### solve 1 - timeout

```python
def truckTour(petrolpumps):
    n = len(petrolpumps)
    idx = [x for x in range(n)]
    p = petrolpumps
    for i in range(n):
        now = idx[i:]+idx[:i]
        tank = 0
        flag = False
        for j in now:
            tank += p[j][0]-p[j][1]
            if tank >= 0:
                flag = True
            else :
                flag = False
                break
        if flag==True:
            return i
```

- 기본적으로 앞에서부터 탐색을 하는게 좋겠다. smallest index를 찾아내는 거니깐
- 우선은 첫번째 petrol이 가능한지부터 보고
- 그 다음에 모든 여행이 가능한지 보아야할듯.
- 첫번째 시도는 4개만 맞고 시간초과남. 자료구조적으로 시간복잡도 개선이 필요함
- 보니깐 자료구조적으로 queue를 사용하라고함.

### solve 2 - 꼼수

```python
def truckTour(petrolpumps):
    n = len(petrolpumps)
    answer = 0
    tank = 0

    for i in range(n):
        petr, dist = petrolpumps[i]
        tank += petr

        if dist <= tank:
            tank -= dist
        else:
            tank = 0
            answer = i+1

    return answer
```

- 사실 queue도 필요없다.
- 기본적으로 한 가지 경우는 반드시 조건을 만족하는 경우가 있다는 것이 문제의 함정이다.
- 그래서 앞에서부터 탱크를 채워가다가 앵꼬가 나는 순간 answer를 해당 경우로 갱신해주면서 한번만 돌아주면 되는 것이다.
- 사실 queue를 이용해서 뒤에 다시 덧붙이면서 해줘야하는데 약간 꼼수로 풀수도 있다는 것이 신기하다.
