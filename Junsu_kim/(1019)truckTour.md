
# [Truck Tour - Queues](https://www.hackerrank.com/challenges/truck-tour/problem?h_r=internal-search)

## 1. problem

Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
An integer which will be **the smallest index** of the petrol pump from which we can start the tour.

## 2. codes

```python
from collections import deque
def truckTour(pp):
    pp = deque(pp)
    temp = pp
    for i in range(len(pp)):
        if is_possible(temp)=='yes':
            return i
            break
        else:
            right = temp.popleft()
            temp.append(right)

def is_possible(now):
    tank = 0
    for i,j in now:
        tank += i
        tank -= j
        if tank >= 0:
            pass
        else:
            return 'no'
            break
    return 'yes'
```

## 3. solve points

1. 가장 작은 수를 찾아내는 것이기 때문에 0 indice 부터 시작하는 것이 가장 효율적이다
2. 그럼 0부터 찾되 , 한 indice를 끝냈을 경우에는 그 자리의 숫자들list를 맨 뒤로 보내는 작업이 필요하다.\
    그렇기 때문에 deque를 사용하는 것이 편했다. 빠르기도 하고. popleft가 필요했기 때문에 deque를 사용했다.
