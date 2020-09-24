def ft_bin_num(a):
    b = 0
    l = 0
    c = 0
    m = a
    if a >= 0:
        while a > 0:
            l = l + 1
            a = a // 10
    if a >= 0:
        while m > 0:
            c = (m % 2) * 10 ** l
            m = m // 2
            l = l - 1
        return c
