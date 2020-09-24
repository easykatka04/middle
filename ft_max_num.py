def ft_max_num(a):
    if a >= 0:
        b = a % 10
        while a > 0:
            a = a // 10
            if b < a % 10:
                b = a % 10
        return b
    if a < 0:
        a = a * -1
        b = a % 10
        while a > 0:
            a = a // 10
            if b < a % 10:
                b = a % 10
        return b