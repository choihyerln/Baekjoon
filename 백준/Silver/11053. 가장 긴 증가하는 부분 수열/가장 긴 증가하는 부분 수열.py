n = int(input())
a = list(map(int, input().split()))
dp = [1] * n

for i in range(n):
    for j in range(i):      # 전에 것들과 비교
        if a[i]>a[j]:       # 현재 값이 더 크면
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))    