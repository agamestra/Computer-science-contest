def f():
    n = 0
    nmax = 0
    def cont(a, x, n, nmax):
        b = int(input())
        if b == 0:
            return nmax
        elif a == b:
            n = 1
            if n > nmax:
                nmax = n
            return cont(a, 0, n, nmax)
        elif a < b:
            if x == 1:
                n += 1
                if n > nmax:
                    nmax = n
            else:
                n = 2
                if n > nmax:
                    nmax = n
            a = b
            return cont(a, 1, n, nmax)
        elif a > b:
            if x == -1:
                n += 1
                if n > nmax:
                    nmax = n
            else:
                n = 2
                if n > nmax:
                    nmax = n
            a = b
            return cont(a, -1, n, nmax)
    a = int(input())
    if a == 0:
        return n
    else:
        n += 1
        if n > nmax:
            nmax = n
        return cont(a, 0, n, nmax)
print(f())