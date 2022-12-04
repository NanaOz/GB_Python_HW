# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print("ЗАДАЧА 1")
num = float(input("Введите число: "))
sum = 0
for i in str(num):
    if i != ".":
        sum += int(i)
print(f'Сумма цифр {num} -> {sum}')

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
print("ЗАДАЧА 2")
n = int(input("Введите число: "))
factorial = 1
listMult = []
for i in range(1, n + 1):
    factorial *= i
    listMult.append(factorial)
print(f"Произведение:  {listMult}")

# 3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму
print("ЗАДАЧА 3")
num = int(input("Введите число: "))
listSequence = {}
sum = 0
for i in range(1, num + 1):
    listSequence[i] = round(((1+1/i)**i), 2)
    sum += listSequence[i]
print(f'Последовательность: {listSequence}. \nСумма {sum}')

# 4. Реализуйте алгоритм перемешивания списка
import random
from random import randint
print("ЗАДАЧА 4")
size = int(input("Введите размер списка: "))
listA = []
for i in range(size):
    listA.append(randint(0, 100))
print(f'Начальный список {listA}')
random.shuffle(listA)
print(f'Список после перемешивания {listA}')