import sys
import heapq as hq
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    deadline, cupNoodle = map(int, input().split())
    array.append((deadline, cupNoodle))

array.sort()

q = []

for i in array:
    hq.heappush(q, i[1])    # 힙에 컵라면 넣어 (최소힙)
    if i[0] < len(q):       # 힙큐의 길이가 데드라인보다 커지면
        hq.heappop(q)       # 컵라면 작은거 pop
print(sum(q))