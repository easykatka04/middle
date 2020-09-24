def ft_bin_num(a):
    c = 0
    if a >= 0:
        while a > 0:
            c = c * 10 + a % 2
            a = a // 2
        return c
