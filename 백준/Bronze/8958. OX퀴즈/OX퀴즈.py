a = int(input())
li = []     # 입력하는 OX들의 리스트
resultLi = []   # 점수계산한 문제들을 담은 리스트

# 인풋값 리스트
for _ in range(a):
    li.append(str(input()))

for i in range(len(li)):
    score = 0
    result = 0
    for j in range(len(li[i])):
        if li[i][j] == "O":
            score += 1
            result += score
        else:
            score = 0
    resultLi.append(result)
    print(resultLi[i])