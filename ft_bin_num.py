def ft_bin_num(a):
    b = 1
    d = 0
    while a > 0:
        d += a % 2 * b
        b *= 10
        a //= 2
    return d
