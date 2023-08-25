n,k = map(int, input().split())
coin_type = []
cnt = 0

for _ in range(n):
    coin_type.append(int(input()))

for coin in reversed(coin_type):
    cnt += k // coin
    k = k % coin
print(cnt)