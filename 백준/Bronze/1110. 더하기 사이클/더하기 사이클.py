n = int(input())
new = n
count = 0
 
while 1:
    a = new // 10
    b = new % 10
    c = (a+b) % 10
    new = (b*10) + c
    count += 1

    if(new == n):
        break
print(count)