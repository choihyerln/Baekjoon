n = int(input())        # 탑의 개수   
tops = list(map(int, input().split()))  # 탑 리스트
stack = []
answer = []

for i in range(n):
    while stack:
        if stack[-1][1] > tops[i]:    # 수신 가능한 상황
            answer.append(stack[-1][0] + 1)     # 인덱스+1 도출
            break
        else:
            stack.pop()
    if not stack:          # 스택이 비어있다면
        answer.append(0)   # 레이저를 수신할 탑이 없다
    stack.append([i, tops[i]])  # 인덱스, 값

print(" ".join(map(str, answer)))