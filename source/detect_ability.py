from gen_errors import gen_errors, get_k_errors_dict, factorial
from decode_vector import error_syndrome


def info_for_k_error(v, n, k):
    err = 0
    errors = gen_errors(n, k)
    total_err = len(errors)  # кол-во ошибок равно числу сочетаний из n по k
    for error in errors:
        damaged_vector = format(int(v, 2) ^ int(error, 2), '07b')
        if error_syndrome(damaged_vector).find('1') != -1:
            err += 1
    return err, total_err, (err * 1.0 / total_err)
