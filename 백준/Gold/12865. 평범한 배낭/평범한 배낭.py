n, k = map(int, input().split())    # 주어지는 물품수, 무게맥시멈
thing = [[0,0]]

for _ in range(n):
    thing.append(list(map(int, input().split())))
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = thing[i][0]
        v = thing[i][1]

        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])
