__author__ = "Evgeny"
def fun():
    n = 1
    mx = int(input())
    while True:
        a = int(input())
        if a == 0:
            return n
        elif a > mx:
            mx = a
            n = 1
        elif a == mx:
            n += 1
print(fun())