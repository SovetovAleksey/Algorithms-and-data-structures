# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
# задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import defaultdict, deque

sixteen = defaultdict()
sixteen['0'] = '0'
sixteen['1'] = '1'
sixteen['2'] = '2'
sixteen['3'] = '3'
sixteen['4'] = '4'
sixteen['5'] = '5'
sixteen['6'] = '6'
sixteen['7'] = '7'
sixteen['8'] = '8'
sixteen['9'] = '9'
sixteen['A'] = '10'
sixteen['B'] = '11'
sixteen['C'] = '12'
sixteen['D'] = '13'
sixteen['E'] = '14'
sixteen['F'] = '15'

value_1 = deque(input('Введите первое число '))
value_2 = deque(input('Введите второе число '))

summa_result = deque()
prod_result = deque()


def summa(value_1, value_2):
    summa_result.clear()
    if len(value_1) > len(value_2):
        for i in range(len(value_1) - len(value_2)):
            value_2.appendleft('0')

    if len(value_2) > len(value_1):
        for i in range(len(value_2) - len(value_1)):
            value_1.appendleft('0')

    if len(value_2) == len(value_1):
        pass

    v_ume = 0

    for i in range(len(value_1)):
        length = len(value_1)
        if value_1[(length - 1) - i] == 'A':
            value_1[(length - 1) - i] = '10'
        if value_1[(length - 1) - i] == 'B':
            value_1[(length - 1) - i] = '11'
        if value_1[(length - 1) - i] == 'C':
            value_1[(length - 1) - i] = '12'
        if value_1[(length - 1) - i] == 'D':
            value_1[(length - 1) - i] = '13'
        if value_1[(length - 1) - i] == 'E':
            value_1[(length - 1) - i] = '14'
        if value_1[(length - 1) - i] == 'F':
            value_1[(length - 1) - i] = '15'

        if value_2[(length - 1) - i] == 'A':
            value_2[(length - 1) - i] = '10'
        if value_2[(length - 1) - i] == 'B':
            value_2[(length - 1) - i] = '11'
        if value_2[(length - 1) - i] == 'C':
            value_2[(length - 1) - i] = '12'
        if value_2[(length - 1) - i] == 'D':
            value_2[(length - 1) - i] = '13'
        if value_2[(length - 1) - i] == 'E':
            value_2[(length - 1) - i] = '14'
        if value_2[(length - 1) - i] == 'F':
            value_2[(length - 1) - i] = '15'

        res = int((int(value_1[(length - 1) - i]) + int(value_2[(length - 1) - i]))) + v_ume

        if res > 25:
            for i, item in sixteen.items():
                if res - 16 == int(item):
                    summa_result.appendleft(i)
            v_ume = 1

        if res > 15 and res <= 25:
            result = (res - 15) - 1
            summa_result.appendleft(str(result))
            v_ume = 1

        if res >= 10 and res <= 15:
            v_ume = 0
            for i, item in sixteen.items():
                if res == int(item):
                    summa_result.appendleft(i)

        if res < 10:
            v_ume = 0
            result = res % 10
            summa_result.appendleft(str(result))

    if v_ume == 0:
        pass
    elif v_ume == 1:
        summa_result.appendleft(str(v_ume))
    return summa_result


def prod():
    global prod_result_copy
    length_1 = int(len(value_1))
    length_2 = int(len(value_2))
    result_list = []
    var_list = []
    v_ume = 0

    for i in range(len(value_1)):
        if value_1[(length_1 - 1) - i] == 'A':
            value_1[(length_1 - 1) - i] = '10'
        if value_1[(length_1 - 1) - i] == 'B':
            value_1[(length_1 - 1) - i] = '11'
        if value_1[(length_1 - 1) - i] == 'C':
            value_1[(length_1 - 1) - i] = '12'
        if value_1[(length_1 - 1) - i] == 'D':
            value_1[(length_1 - 1) - i] = '13'
        if value_1[(length_1 - 1) - i] == 'E':
            value_1[(length_1 - 1) - i] = '14'
        if value_1[(length_1 - 1) - i] == 'F':
            value_1[(length_1 - 1) - i] = '15'

        for j in range(len(value_2)):
            if value_2[(length_2 - 1) - j] == 'A':
                value_2[(length_2 - 1) - j] = '10'
            if value_2[(length_2 - 1) - j] == 'B':
                value_2[(length_2 - 1) - j] = '11'
            if value_2[(length_2 - 1) - j] == 'C':
                value_2[(length_2 - 1) - j] = '12'
            if value_2[(length_2 - 1) - j] == 'D':
                value_2[(length_2 - 1) - j] = '13'
            if value_2[(length_2 - 1) - j] == 'E':
                value_2[(length_2 - 1) - j] = '14'
            if value_2[(length_2 - 1) - j] == 'F':
                value_2[(length_2 - 1) - j] = '15'

            res = int(int(value_1[(length_1 - 1) - i]) * (int(value_2[(length_2 - 1) - j]))) + v_ume
            v_ume = res // 16

            for k, item in sixteen.items():
                if v_ume == 0 and res == int(item):
                    prod_result.appendleft(k)
                if v_ume > 0 and res % 16 == int(item):
                    prod_result.appendleft(k)

        prod_result.appendleft(str(v_ume))

        while i != 0:
            prod_result.append('0')
            i -= 1

        prod_result_copy = prod_result.copy()
        v_ume = 0

        result_list.append(prod_result_copy)
        prod_result.clear()

    for m in range(len(value_1)):
        var_m = result_list[m]
        var_list.append(var_m)

    var_last = var_list[len(var_list) - 1]

    for e in range(len(var_list)):
        while len(var_list[e]) < len(var_last):
            var_list[e].appendleft('0')

    t = 1

    while len(var_list) != 1:
        summa(var_list[t - 1], var_list[t])
        summa_result_new = summa_result.copy()
        var_list[t] = summa_result_new
        summa_result.clear()
        var_list.pop(t - 1)

    final = var_list[0]
    while final[0] == '0':
        final.popleft()
    print(f'Результат умножения - {final}')


print(f'Результат сложения - {summa(value_1, value_2)}')
prod()
