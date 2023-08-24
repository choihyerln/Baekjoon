import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
maxi = 100001
visited = [0] * maxi

def bfs(x):
    queue = deque([x])
    while queue:
        x = queue.popleft()
        
        if x == k:
            return visited[x]

        for next_x in (x-1, x+1, 2*x):
            if  0 <= next_x < maxi and not visited[next_x]:
                visited[next_x] = visited[x] + 1
                queue.append(next_x)

print(bfs(n))