# 1. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
from math import pi

print("ЗАДАЧА 1")
d = float(input("Введите число в пределах от 0.1 до 0.0000000001: "))


def fractional_part_len(number_to_count):
    count = 0

    while number_to_count % 1 != 0:
        number_to_count *= 10
        count += 1

    return count


if pow(10, -1) >= d >= pow(10, -10):
    new_d = fractional_part_len(d)
    print(f'число π с заданной точностью {d} = {round(pi, new_d)}')
else:
    print("Число не соответствует условию: от 0.1 до 0.0000000001")

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
print("ЗАДАЧА 2")
n = int(input("Введите число: "))


def multipliers(number):
    one_mult = 2
    some_list = []
    while one_mult <= number:
        if number % one_mult == 0:
            some_list.append(one_mult)
            number //= one_mult
            one_mult = 2
        else:
            one_mult += 1
    print(f"Простые множители = {some_list}")


multipliers(n)

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
print("ЗАДАЧА 3")
some_list = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Заданный список: {some_list}")
new_some_list = []
for i in some_list:
    if i not in new_some_list:
        new_some_list.append(i)
print(f"Неповторяющиеся элементы: {new_some_list}")

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

print("ЗАДАЧА 4")

k = int(input("Введите натуральную степень: "))
ratio = []
for i in range(k + 1):
    ratio.append(random.randint(0, 100))


def create_polynomial(some_list):
    result = ""
    if len(some_list) < 1:
        result = "x = 0"
    else:
        for i in range(len(some_list)):
            if i != len(some_list) - 1 and some_list[i] != 0 and i != len(some_list) - 2:
                result += f"{some_list[i]}x^{len(some_list) - i - 1}"
                if some_list[i + 1] != 0:
                    result += " + "
            elif i == len(some_list) - 2 and some_list[i] != 0:
                result += f"{some_list[i]}x"
                if some_list[i + 1] != 0:
                    result += " + "
            elif i == len(some_list) - 1 and some_list[i] != 0:
                result += f"{some_list[i]} = 0"
            elif i == len(some_list) - 1 and some_list[i] == 0:
                result += " = 0"
    return result


def write_file(name, st):
    with open(name, 'w') as data:
        data.write(st)


write_file("file.txt", create_polynomial(ratio))
print("Уравнение записано в файл!")