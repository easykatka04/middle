def ft_sum_num(a):
    b = 0
    if a >= 0:
        while a > 0:
            b = b + (a % 10)
            a = a // 10
        return b
    if a < 0:
        a = a * -1
        while a > 0:
            b = b + (a % 10)
            a = a // 10
        return b
