def fun():
    l = 0
    lmin = 0
    a = int(input())
    b = int(input())
    if a == 0 or b == 0:
        return 0
    while True:
        c = int(input())
        if c == 0:
            return lmin
        if a < b > c:
            if l != 0:
                if lmin == 0:
                    lmin = l
                elif l < lmin:
                    lmin = l
                l = 1
            else:
                l = 1
        elif l > 0:
            l += 1
        a, b = (b, c)
print(fun())