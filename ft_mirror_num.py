def ft_mirror_num(a):
    b = a
    c = 0
    if a < 0:
        a = -a
        b = a
        c = 0
        while a > 0:
            b = a % 10
            c = c * 10 + b
            a //= 10

        if c == b:
            return True
        return False
