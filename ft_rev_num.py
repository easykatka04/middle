def ft_rev_num(a):
    c = 0
    if a >= 0:
        while a > 0:
            c = c * 10 + a % 10
            a = a // 10
        return c
    if a < 0:
        a = a * -1
        while a > 0:
            c = c * 10 + a % 10
            a = a // 10
        return -c