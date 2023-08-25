ex = input().split('-')
num = []    # - 기준으로 나눈 항들의 합을 저장할 리스트

for i in ex:
    tmp = 0
    for j in i.split('+'):      # + 연산하는 숫자들의 합 tmp에 넣어줌
        tmp += int(j)
    num.append(tmp)

for i in range(1, len(num)):
    num[0] = num[0] - num[i]
print(num[0])