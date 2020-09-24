def ft_mirror_num(a):
    b = a
    c = 0
    if a < 0:
        a = -a
        b = a
        c = 0
        while a > 0:
            f = a % 10
            c = c * 10 + f
            a //= 10

        if c == b:
            return True
        return False

    while a > 0:
        f = a % 10
        c = c * 10 + f
        a //= 10

    if c == b:
        return True
    return False


def ft_mirror_count(a):
    n = 0
    for i in range(1, a + 1):
        if ft_mirror_num(i) is True:
            n += 1
    return n
