N, M = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(N)]

# dp 첫번째 행 업데이트
for i in range(1, M):
    dp[0][i] += dp[0][i-1]

# 나머지 행 업데이트
for i in range(1, N):
    left_to_right = dp[i][:]    # 왼쪽에서 오른쪽으로 가는 경우
    right_to_left = dp[i][:]    # 오른쪽에서 왼쪽으로 가는 경우

    # 왼쪽 -> 오른쪽
    for j in range(M):
        # 첫번째 열은 위에서 오는 경우만 있음
        if j==0:
            left_to_right[j] += dp[i-1][j]
        # 나머지 열 : 위에서 내려오는 경우와 왼쪽에서 오는 경우 비교
        else:
            left_to_right[j] += max(dp[i-1][j], left_to_right[j-1])
    
    # 오른쪽 -> 왼쪽
    for j in range(M-1, -1, -1):
        # 마지막 열은 위에서 오는 경우만 있음
        if j==M-1:
            right_to_left[j] += dp[i-1][j]
        # 나머지 열 : 위에서 내려오는 경우와 오른쪽에서 오는 경우 비교
        else:
            right_to_left[j] += max(dp[i-1][j], right_to_left[j+1])
    
    # 두 가지 임시 배열을 비교해 각 좌표값들을 최대값으로 업데이트
    for j in range(M):
        dp[i][j] = max(left_to_right[j], right_to_left[j])
        
print(dp[N-1][M-1])