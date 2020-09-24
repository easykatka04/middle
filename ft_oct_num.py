def ft_oct_num(a):
    b = 1
    d = 0
    while a > 0:
        d += a % 8 * b
        b *= 10
        a //= 8
    return d
