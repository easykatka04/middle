def ft_rev_bin_num(a):
    c = 0
    l = 0
    k = 1
    c = c + (a % 10)
    l = l + 1
    while a > 0:
        c = c + (a % 10 * k)
        k = k * 2
        a = a // 10
    return c
