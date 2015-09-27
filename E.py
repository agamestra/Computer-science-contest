__author__ = "Evgeny"
def fun():
    mx = int(input())
    mx2 = int(input())
    if mx2 > mx:
        mx, mx2 = (mx2, mx)
    while True:
        a = int(input())
        if a == 0:
            return mx2
        if a > mx:
            mx, mx2 = (a, mx)
        elif a > mx2:
            mx2 = a
print(fun())