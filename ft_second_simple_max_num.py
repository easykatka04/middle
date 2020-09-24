def ft_second_simple_max_num(a):
    d = 0
    b = 0
    c = a
    while c > 0:
        if d < c % 10:
            d = c % 10
        c //= 10

    while a > 0:
        if d >= b < a % 10:
            b = a % 10
        a //= 10

    if b == d:
        return -1
