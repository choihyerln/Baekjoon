n = int(input())    # 추의 개수
weights = list(map(int, input().split()))

m = int(input())    # 구슬의 개수
marbles = list(map(int, input().split()))

dp = [0]*(30*500+1)
for weight in weights:
    tmp = []
    for i in dp:
        tmp.append(i+weight)
        tmp.append(abs(i-weight))
    dp = list(set(dp+tmp))

for marble in marbles:
    if marble in dp:
        print('Y', end=' ')
    else:
        print('N')