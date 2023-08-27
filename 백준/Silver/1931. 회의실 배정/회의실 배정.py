n = int(input())
meeting = []
for _ in range(n):
    s,e = list(map(int, input().split()))
    meeting.append([s,e])
meeting.sort(key=lambda meeting: (meeting[1], meeting[0]))    # 끝나는 시간 기준으로 정렬

end_time = meeting[0][1]    
cnt = 1 # 첫번째 회의

for i in range(1, n):
    if meeting[i][0] >= end_time:
        cnt += 1
        end_time = meeting[i][1]
print(cnt)