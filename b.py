def binpow1(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return binpow1(a, n - 1) * a
    else:
        return binpow1(a, n / 2) * binpow1(a, n / 2)


def myPow(self, x, n):
    if n >= 0:
        return binpow1(x, n)
    else:
        return float(1) / binpow1(x, n)
print