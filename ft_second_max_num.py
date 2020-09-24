def ft_len_num(a):
    v = 0
    if a < 0:
        a = -a
    while a > 0:
        a += 1
        a //= 10
    return v


def ft_second_max_num(a):
    k = 0
    n = 0
    z = a

    while z > 0:
        if k < z % 10:
            k = z % 10
        z //= 10

    while a > 0:
        if k > a % 10 > n:
            n = a % 10
        a //= 10

    return n
