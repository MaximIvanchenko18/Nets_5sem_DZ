def get_checked_pos(pattern, one_pos):
    num = 1
    summa = 0
    for symbol in list(reversed(pattern)):
        if format(num, '03b')[-one_pos] == '1' and symbol != ' ':
            summa += int(symbol)
        num += 1
    summa %= 2
    return summa


def code_vector(v):
    res = list(v)
    res.append(' ')  # проверочный разряд 001
    res.insert(-1, ' ')  # проверочный разряд 010
    res.insert(-3, ' ')  # проверочный разряд 100
    res[-1] = str(get_checked_pos(res, 1))
    res[-2] = str(get_checked_pos(res, 2))
    res[-4] = str(get_checked_pos(res, 3))
    return ''.join(res)
