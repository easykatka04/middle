def ft_max_num(a):
    b = 0
    if a < 0:
        a = -a
    while a > 0:
        if b < (a % 10):
            b = (a % 10)
        a //= 10
    return b
