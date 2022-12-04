# 1. Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('ЗАДАЧА 1')
someList = list(map(int, input('Введите числа через пробел:\n').split()))
sum = 0
listOdd = []
for i in range(len(someList)):
    if i % 2 != 0:
        sum += someList[i]
        listOdd.append(someList[i])
print(f'Нечетные числа: {listOdd}.\nСумма = {sum}')

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]
print('\nЗАДАЧА 2')
myList = list(map(int, input('Введите числа через пробел:\n').split()))
newList = []
if len(myList) % 2 != 0:
    half = len(myList) // 2 + 1
    for i in range(half):
        newList.append(myList[i]*myList[len(myList)-i-1])
else:
    half = len(myList) // 2
    for i in range(half):
        newList.append(myList[i] * myList[len(myList) - i - 1])
print(newList)

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов.
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
print('\nЗАДАЧА 3')
fracList = list(map(float, input('Введите вещественные числа через пробел:\n').split()))
newFracList = []
for i in fracList:
    if i % 1 != 0:
        newFracList.append(round(i % 1, 2))
print(f'Разница между Max и Min значением дробной части = {max(newFracList) - min(newFracList)}')

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное
# 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print('\nЗАДАЧА 4')
num = int(input('Введите число, чтобы перевести его в двоичное:\n'))
binaryNum = ''
while num != 0:
    binaryNum = str(num % 2) + binaryNum
    num //= 2
print(binaryNum)

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
print('\nЗАДАЧА 5')
n = int(input('Введите число: '))
i = fib_0 = 0
fib_1 = fib_2 = fib_n2 = 1
fib_n1 = -1
fibList = [fib_n1, fib_1, fib_0, fib_1, fib_2]
while i < n - 2:
    fib_sum_pos = fib_1 + fib_2
    fib_sum_neg = fib_n2 - fib_n1
    fib_1 = fib_2
    fib_2 = fib_sum_pos
    fib_n2 = fib_n1
    fib_n1 = fib_sum_neg
    fibList.append(fib_sum_pos)
    fibList.insert(0, fib_sum_neg)
    i = i + 1
print(fibList)