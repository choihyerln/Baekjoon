import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    grade = []
    n = int(input())
    for _ in range(n):
        d, i = list(map(int, input().split()))
        grade.append([d,i])

    grade.sort(key=lambda grade: grade[0])

    start = grade[0][1]
    cnt = 1

    for a, b in grade:
        if b < start:
            cnt += 1
            start = b
    print(cnt)