a = int(input())
b = input()

c = []
for i in range(3):
    c.append(a*int(b[i]))
c.reverse()
d = c[0]+c[1]*10+c[2]*100
c.append(d)

for i in range(4):
    print(c[i])