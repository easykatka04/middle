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
def ft_second_max_num(a):
    if a >= 0:
        b = 0
        while a > 0:
            if b < a % 10 and (a % 10 != ft_max_num):
                b = a % 10
            a = a // 10
        return b
    if a < 0:
        a = a * -1
        b = 0
        while a > 0:
            if b < a % 10 and (a % 10 != ft_max_num)
                b = a % 10
            a = a // 10
        return b