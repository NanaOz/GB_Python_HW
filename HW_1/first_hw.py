# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли
# этот день выходным
print("ЗАДАЧА 1")
day = int(input("Введите число: "))
if day == 6 or day == 7:
    print("Это выходной")
elif 0 < day < 6:
    print("Это будний день")
else:
    print("Нет такого дня")

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
print("ЗАДАЧА 2")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            print((not(x or y or z)) == (not x and not y and not z))

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print("ЗАДАЧА 3")
x = int(input("Введите координату X: "))
y = int(input("Введите координату Y: "))
print(f"Координаты: [{x};{y}]")
if x == 0 and y == 0:
    print("Ошибка!Введите другие координаты!")
elif x > 0 and y > 0:
    print("I четверть")
elif x < 0 and y > 0:
    print("II четверть")
elif x < 0 and y < 0:
    print("III четверть")
elif x == 0 and y != 0:
    print("Точка лежит на оси Y")
elif x!= 0 and y == 0:
    print("Точка лежит на оси X")
else:
    print("IV четверть")

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в
# этой четверти (x и y).
print("ЗАДАЧА 4")
part = int(input("Введите номер четверти: "))
if part == 1:
    print("Диапазон возможных координат точек: (x > 0; y > 0)")
elif part == 2:
    print("Диапазон возможных координат точек: (x < 0; y > 0)")
elif part == 3:
    print("Диапазон возможных координат точек: (x < 0; y < 0)")
elif part == 4:
    print("Диапазон возможных координат точек: (x > 0; y < 0)")
else:
    print("Такой четверти не существует!")

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
# в 2D пространстве
import math

print("ЗАДАЧА 5")
print("Введите координаты первой точки:")
x1, y1 = map(int, input().split(', '))
print("Введите координаты второй точки:")
x2, y2 = map(int, input().split(', '))
print(f"Координаты первой точки: [{x1};{y1}] \nКоординаты второй точки: [{x2};{y2}]")
distance = round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)
print(f"Расстояние между точками = {distance}")