def ft_len_num(a):
    b = 0
    while a > 0:
        b = b + 1
        a = a // 10
    return b
