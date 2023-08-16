x,y,w,h = map(int, input().split())

m = min(x, y, (w-x), (h-y))
print(m)