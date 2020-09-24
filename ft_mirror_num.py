def ft_mirror_num(a):
    c = 0
    l = a
    if a >= 0:
        while a > 0:
            c = c * 10 + a % 10
            a = a // 10
    if a < 0:
        a = a * -1
        while a > 0:
            c = c * 10 + a % 10
            a = a // 10
    if c == l:
        print("TRUE")
    if c != l:
        print("FALSE")