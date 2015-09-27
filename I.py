__author__ = "Evgeny"
def fun():
    n = 0
    a = int(input())
    b = int(input())
    if a == 0 or b == 0:
        return 0
    while True:
        c = int(input())
        if c == 0:
            return n
        if a < b > c:
            n += 1
        a, b = (b, c)
print(fun())