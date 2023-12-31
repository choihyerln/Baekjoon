n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))

dp = [10001] * (k+1)     # 최소값 구하는 DP 이므로 k최대값으로 초기화
dp[0] = 0

for i in range(n):
    for j in range(coins[i], k+1):
        # if dp[j-coins[i]] != 10001: 
        dp[j] = min(dp[j], dp[j-coins[i]]+1)

if dp[k] == 10001:
    print(-1)

else:
    print(dp[k])