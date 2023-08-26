a = ' ' + input()
b = ' ' + input()
dp = [[0] * len(b) for _ in range(len(a))]
dpstr = [['']*len(b) for _ in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dpstr[i][j] = dpstr[i-1][j-1]+a[i]
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            if dp[i-1][j] > dp[i][j-1]:
                dp[i][j] = dp[i-1][j]
                dpstr[i][j] = dpstr[i-1][j]
            else: 
                dp[i][j] = dp[i][j-1]
                dpstr[i][j] = dpstr[i][j-1]

print(dp[-1][-1])
if dp[-1][-1] != 0:
    print(dpstr[-1][-1])