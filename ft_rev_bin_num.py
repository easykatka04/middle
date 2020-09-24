def ft_pow(a, s):
    b = a
    if s > 0:
        for i in range(s - 1):
            a *= b
        return a
    elif s == 0:
        return 1
    for i in range(a):
        a /= b
    return a


def ft_rev_bin_num(a):
    c = a
    v = 0
    d = 0
    while c > 0:
        c //= 10
        d += 1
    for digit in range(d):
        v += a % 10 * ft_pow(2, digit)
        a //= 10
    return v


