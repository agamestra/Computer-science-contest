__author__ = "Evgeny"
def fun():
    n = 1
    nmax = 1
    flag = 0
    a = int(input())
    while True:
        b = int(input())
        if b == 0:
            return nmax
        if b < a:
            if flag == -1:
                n += 1
                if n > nmax:
                    nmax = n
            else:
                n = 2
                if n > nmax:
                    nmax = n
                flag = -1
        elif b == a:
            n = 1
            flag = 0
        else:
            if flag == 1:
                n += 1
                if n > nmax:
                    nmax = n
            else:
                n = 2
                if n > nmax:
                    nmax = n
                flag = 1
        a = b
print(fun())