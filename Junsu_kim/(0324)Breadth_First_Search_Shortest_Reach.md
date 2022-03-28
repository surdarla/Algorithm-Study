# [Breath First Search : shortest Reach](https://www.hackerrank.com/challenges/bfsshortreach/problem?isFullScreen=true)

- BFS(breadth-first search) 너비우선탐색
- [지리는 solution](https://www.thepoorcoder.com/hackerrank-breadth-first-search-shortest-reach-solution/)

```python
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n : number of nodes
#  2. INTEGER m : number of edges - edge == 6
#  3. 2D_INTEGER_ARRAY edges : start and end nodes for edges
#  4. INTEGER s : starting node


from queue import Queue

class Node():
    def __init__(self):
        self.distance = -1
        self.children = []
        self.visited = False

def bfs(n, m, edges, s):
    nodes = [Node() for _ in range(n)]
    for edge in edges:
        first, second = [nodes[i - 1] for i in edge]
        first.children.append(second)
        second.children.append(first)
    
    top = nodes[s - 1]
    top.distance = 0
    queue = Queue()
    queue.put(top)
    while(not queue.empty()):
        node = queue.get()
        for child in node.children:
            if (not child.visited) or (child.distance > node.distance + 6):
                child.distance = node.distance + 6
                child.visited = True
                queue.put(child)
    del nodes[s - 1]
    return [node.distance for node in nodes]
```

## Queue - First in First out, BFS, O(1-추가삭제) O(n-search)

- [blog 정리](https://www.daleseo.com/python-queue/)
- [queue python docs](https://docs.python.org/ko/3.7/library/queue.html)
- list, deque, Queue()