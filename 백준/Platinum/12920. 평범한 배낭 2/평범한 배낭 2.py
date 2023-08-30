import sys
input = sys.stdin.readline

N, M = map(int, input().split())    # 물품의 종류 수, 무게 맥시멈
# weight, satisfaction = [], []       # 무게, 만족도
arr = []
for _ in range(N):
    # 물건 무게 V, 만족도 C, 개수 K
    arr.append(list(map(int, input().split())))

dp = [0]*(M+1)

for w, v, k in arr:
    idx = 1
    satisfaction = []
    while k > 0:
        tmp = min(idx, k)
        satisfaction.append(tmp)
        idx *= 2
        k -= tmp

    for pick in satisfaction:
        for weight in range(M, 0, -1):
            if weight < w * pick:
                break
            else:
                dp[weight] = max(dp[weight], dp[weight-w*pick]+v*pick)
print(dp[M])