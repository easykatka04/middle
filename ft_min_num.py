def ft_min_num(a):
    l = 10
    c = 0
    if a >= 0:
        while a > 0 and a % 1 == 0:
            b = a % 10
            if b < l:
                l = b
            a = a // 10
        return l
    if a < 0 and a % 1 == 0:
        a = a * -1
        while a > 0:
            b = a % 10
            if b < l:
                l = b
            a = a // 10
        return l
