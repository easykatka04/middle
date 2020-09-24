def ft_null_count(a):
    c = 0
    if a >= 0:
        while a > 0:
            if a % 10 == 0:
                c = c + 1
            a = a // 10
        return c
    if a < 0:
        a = a * -1
        while a > 0:
            if a % 10 == 0:
                c = c + 1
            a = a // 10
        return c
