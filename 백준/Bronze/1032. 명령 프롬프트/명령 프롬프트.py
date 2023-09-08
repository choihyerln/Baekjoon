n = int(input())
word_1 = list(input())

for _ in range(n-1):
    word_2 = input()
    for i in range(len(word_1)):
        if word_1[i] == word_2[i]:
            continue
        else:
            word_1[i] = "?"
print(*word_1,sep='')