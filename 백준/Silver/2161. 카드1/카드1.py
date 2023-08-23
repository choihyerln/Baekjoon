import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])
answer = []

for i in range(n):
    queue.append(i+1)

while len(queue) > 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())
print(*answer, queue[0])