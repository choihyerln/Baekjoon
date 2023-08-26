import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
m = int(input())

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for gap in range(2, n):
    for start in range(n-gap):
        if nums[start] == nums[start+gap]:
            if dp[start+1][start+gap-1] == 1:
                dp[start][start+gap] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
