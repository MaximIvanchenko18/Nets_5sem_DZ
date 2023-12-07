def error_syndrome(v):
    ind = 3
    res = []
    while ind > 0:
        summa = 0
        cnt = 1
        for symbol in v[::-1]:
            if format(cnt, '3b')[-ind] == '1':
                summa += int(symbol)
            cnt += 1
        summa %= 2
        res.append(str(summa))
        ind -= 1
    return ''.join(res)


def correct_damaged_vector_1_error(v):
    err_syndrome_num = int(error_syndrome(v), 2)
    corrected_vector = format(int(v, 2) ^ int('1' + '0' * (err_syndrome_num - 1), 2), '07b')
    return corrected_vector


def decode_damaged_vector(v):
    corrected_vector = correct_damaged_vector_1_error(v)
    res = corrected_vector[:3] + corrected_vector[4]
    return res
