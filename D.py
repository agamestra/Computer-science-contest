def fun():
    mx = int(input())
    while True:
        a = int(input())
        if a == 0:
            return mx
        if a > mx:
            mx = a
print(fun())