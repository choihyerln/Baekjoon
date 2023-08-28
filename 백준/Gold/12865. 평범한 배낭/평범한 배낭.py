n, k = map(int, input().split())  # 주어지는 물품수, 무게맥시멈
thing = []

for _ in range(n):
    thing.append(list(map(int, input().split())))

dp = [0]*(k+1)

for w, v in thing:
    for weight in range(k, 0, -1):
        if w <= weight:
            dp[weight] = max(dp[weight], dp[weight-w]+v)
        else:
            break
print(dp[-1])