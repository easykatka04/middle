def ft_second_max_num(a):
    b = 0
    c = a
    l = 0
    if a >= 0 and a % 1 == 0:
        while a > 0:
            if b < a % 10:
                b = a % 10
            a = a // 10
    if a < 0 and a % 1 == 0:
        a = a * -1
        while a > 0:
            if b < a % 10:
                b = a % 10
            a = a // 10
    if c >= 0 and c % 1 == 0:
        while c > 0:
            if l < c % 10 and c % 10 != b:
                l = c % 10
            c = c // 10
        return l
    if c < 0 and c % 1 == 0:
        c = c * -1
        while c > 0:
            if l < c % 10 and c % 10 != b:
                l = c % 10
            c = c // 10
        return l
