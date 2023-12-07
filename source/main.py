import pandas as pd
from tabulate import tabulate
from code_vector import code_vector
from decode_vector import decode_damaged_vector, correct_damaged_vector_1_error, error_syndrome
from detect_ability import info_for_k_error


def main():
    n = 7  # длина кодовой комбинации Х[7,4]
    vector = input('Enter info vector v : ')  # ввод информационного вектора
    coded_vector = code_vector(vector)
    print("Encoded vector v' = " + coded_vector)
    e = input('Enter error vector e: ')
    damaged_vector = format(int(coded_vector, 2) ^ int(e, 2), '07b')
    print("Now damaged vector v'' = " + damaged_vector)
    print("Error syndrome E = " + error_syndrome(damaged_vector))
    print("Corrected vector v'' = " + correct_damaged_vector_1_error(damaged_vector))
    print("Decoded vector v = " + decode_damaged_vector(damaged_vector))
    print('------------------------------------------------------------------------------------------')
    output_table(coded_vector, n)


def output_table(coded_v, n):
    table = []
    for i in range(1, n + 1):
        row = [i] + list(info_for_k_error(coded_v, n, i))
        table.append(row)
    pd.set_option("display.precision", 4)
    df = pd.DataFrame(table, columns=['Кратность, k', 'Число обнаруженных ошибок, N0', 'Общее число ошибок, Ckn',
                                      'Обнаруживающая способность, C0'])
    print(tabulate(df, showindex=False, headers=df.columns))


if __name__ == '__main__':
    main()
