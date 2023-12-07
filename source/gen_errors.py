def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x - 1)


def is_k_error(num, k):
    while k > 0 and num > 0:
        num &= num - 1
        k -= 1
    if num == 0 and k == 0:
        return True
    return False


def gen_errors(n, k):
    res = []
    limit = factorial(n) / (factorial(n - k) * factorial(k))  # сочетание из n по k
    num = 1
    while len(res) < limit:
        if is_k_error(num, k):
            res.append(format(num, 'b'))
        num += 1
    return res


# для вывода на экран
def get_k_errors_dict(n, k):
    res = {}
    for cur in range(1, k + 1):
        res[cur] = gen_errors(n, cur)
    return res
