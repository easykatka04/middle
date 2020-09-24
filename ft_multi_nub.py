def ft_multi_num(a):
    b = 1
    if a >= 0 and a % 1 == 0:
        while a > 0:
            b = b * (a % 10)
            a = a // 10
        return b
    if a < 0 and a % 1 == 0:
        a = a * -1
        while a > 0:
            b = b * (a % 10)
            a = a // 10
        return b
