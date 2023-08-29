N, K = map(int, input().split())
elec = list(map(int, input().split()))

plug = []
ans = 0

for i in range(K):
    if elec[i] in plug:     # 이미 꽂아져 있으면 컨티뉴
        continue
    
    if len(plug) < N:       # 꽂을 플러그 있으면
        plug.append(elec[i]) 
        continue
    
    indexs = []
    for j in range(N):
        try:
            idx = elec[i:].index(plug[j])   # 꽂아져있는 것들중 다음에 또 나오는 거 인덱스 번호 추출
        except:
            idx = 101   # 다음 사용순서 없다면 사용횟수 최댓값보다 큰 값 저장하여 사용할 일이 없다고 표시해줌
        
        indexs.append(idx)  # 또 나올 제품 인덱스 indexs 배열에 저장
    
    pull_out = indexs.index(max(indexs))    # 가장 나중에 나올 제품의 indexs 배열에서의 인덱스
    del plug[pull_out]        # 플러그에서 일단 뽑아 (제일 나중에 나오니까)
    plug.append(elec[i])      # 플러그에 사용할 전기용품 새로 추가    
    ans += 1                  # 플러그 뺀거 +1

print(ans)