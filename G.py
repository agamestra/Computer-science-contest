maxn = 1
n = 1
a = int(input())
while True:
    b = int(input())
    if b == 0:
        break
    if b == a:
        n += 1
        if n > maxn:
            maxn = n
    else:
        n = 1
    a = b
print(maxn)