S = input()
A = []
a = int(input())
for _ in range(a):
    A.append(input())

result = 0
dp = [0] * 101

def sol(idx):
    global result
    if idx == len(S):
        result = 1
        return
    
    if dp[idx]:     # dp[idx]가 0이 아니고 값이 있으면 이미 검사한 경우이므로
        return      # 리턴
    
    dp[idx] = 1     # 검사할거니까 1로 셋팅

    for i in range(len(A)):
        if len(S[idx:]) >= len(A[i]):   # S가 A[i]보다 더 길 때만 비교 가능
            for j in range(len(A[i])):  # A에 포함된 각 단어의 길이
                if A[i][j] != S[idx+j]: # A[i] 단어와 글자 하나하나를 S와 비교
                    break
            else:
                sol(idx+len(A[i]))  # 찾은 문자 다음 인덱스부터 찾아라
    return
sol(0)
print(result)