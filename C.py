def fun():
    n = 0
    a = int(input())
    if a == 0:
        return n
    while True:
        b = int(input())
        if b == 0:
            return n
        if b > a:
            n += 1
        a = b
print(fun())