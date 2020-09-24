def  ft_oct_num(a):
    c = 0
    if a >= 0:
        while a > 0:
            c = c * 10 + a % 8
            a = a // 8
        return c
