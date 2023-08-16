n, k = map(int, input().split())
x = [int(input()) for _ in range(n)]


start = min(x)
end = start+k

result = 0
while start <= end:
    mid = (start+end)//2
    hap = 0
    for i in x:
        if mid > i:
            hap += (mid - i)

    if hap <= k:
        start = mid + 1
        result = max(result, mid)
    else:
        end = mid - 1
print(result)