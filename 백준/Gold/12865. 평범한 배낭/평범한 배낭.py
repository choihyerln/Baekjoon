n, k = map(int, input().split())
thing = []

for _ in range(n):
    thing.append(list(map(int, input().split())))

dp = [0]*(k+1)

for w,v in thing:
    for weight in range(k, 0, -1):
        if weight < w:
            break
        else:
            dp[weight] = max(dp[weight], dp[weight-w]+v)
print(dp[-1])