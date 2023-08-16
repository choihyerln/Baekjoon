c = int(input())
arr = [list(map(int, input().split())) for _ in range(c)]

for i in arr:
    avg = sum(i[1:])/i[0]

    count = 0
    for j in i[1:]:
        if j > avg:
            count += 1
    print(f"{count/i[0]*100:.3f}%")