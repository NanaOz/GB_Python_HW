## HW_1 
1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли
этот день выходным

2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
четверти плоскости, в которой находится эта точка (или на какой оси она находится).

4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в
этой четверти (x и y).

5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними
в 2D пространстве

## HW_2
1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

3. Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму

4. Реализуйте алгоритм перемешивания списка

## HW_3
1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции
*[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12*

2. Напишите программу, которая найдёт произведение пар чисел списка.Парой считаем первый и последний элемент, второй и предпоследний и т.д.
*[2, 3, 4, 5, 6] => [12, 15, 16];*
*[2, 3, 5, 6] => [12, 15]*

3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
максимальным и минимальным значением дробной части элементов.
*[1.1, 1.2, 3.1, 5, 10.01] => 0.19*

4. Напишите программу, которая будет преобразовывать десятичное число в двоичное
*45 -> 101101*
*3 -> 11*
*2 -> 10*

5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов
*для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]*

## HW_4
1. Вычислить число c заданной точностью d
Пример:
*при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$*

2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
Пример:
*k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0*

## HW_5
1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

2. Создайте программу для игры в ""Крестики-нолики""

3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.

## HW_6

1. Планеты вращаются вокруг звезд по эллиптическим орбитам. Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь
Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит найдет ту, по которой вращается самая далекая планета. 
Круговые орбиты не учитывайте: вы знаете, что у вашей звезды таких планет нет, зато исскуственные спутники были запущены на круговые орбиты
Результатом функции должен быть кортеж, содержащий длинны полуосей эллипса орбиты самой далекой планеты.
Каждая орбита представляет собой кортеж из пары чисел - полуосей ее элипса.
Площадь эллипса вычисляется по формуле S = (pi)ab, где a и b - длинны полуосей эллипса.
При решении задачи используйте списочные выражения.
Подсказка: проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса, а затем найти и сам эллипс, имеющий такую площадь.
Гарантируется, что самая далекая планета ровно одна
Пример:
ввод:
orbit = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
вывод: 2.5 10

2. Напишите функцию same_by(characteristic, objects), которая проверяет, все ли объекты имеют одинаковые значения некоторой характеристики, и возвращает True, 
если это так. Если значение характеристики для разных объектов отличается - то False. Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Пример:
ввод: values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
  print("same")
else:
  print("different")
  вывод: same
Пример 2:
ввод: values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
  print("same")
else:
  print("different")
  вывод: different

3. Вам уже приходилось писать таблицу умножения. Но на этот раз вас попросили сделать в плюс к таблице умножения еще и таблицу сложения, а так же таблицу возведения в
степень.
Чтобы не копировать один и тот же код и обобщить все три функции до единой функции рисования таблиц (бинарных) арифметических операций, напишите функцию print_operation_table(operation, num_rows=9, num_columns=9), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столюцов идет с единицы 
(подумайте, почему не с 0).
Примечание: бинарной операцие называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.


## HW_7  [гит телефонного справочника](https://github.com/NanaOz/GB_python_TelephoneDirectory_HW7)
Задание в группах: Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
- *под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи, пустая строка - разделитель*   
    *Фамилия_1*
    *Имя_1*
    *Телефон_1*
    *Описание_1*
    *Фамилия_2*
    *Имя_2*
    *Телефон_2*
    *Описание_2*
    *и т.д.в файле на одной строке хранится все записи, символ разделитель - **;***
    
    *Фамилия_1,Имя_1,Телефон_1,Описание_1*
    *Фамилия_2,Имя_2,Телефон_2,Описание_2*
    *и т.д.*
## HW_8
1. Отдал ракету в ремонт. Прошлый раз слишком близко подошел к Солнцу; весь лак облез. Завмастерской убеждает купить электрический мозг. У него один есть, вполне приличный,почти не бывший в употреблении, мощностью двенадцать паровых душ.
Напишите программу для определения безопасных дат сближения с Солнцем в зависимости от наличия мозга.Если мозг есть, то каждое третье сближение безопасное (на двух предыдущих он успевает научиться). Если мозга нет, то безопасные только те сближения, что попадают на четверг.

Формат ввода:
Вводится начальная дата – последнее сближение с Солнцем (не рассматривается как подходящая).
Затем вводится 1 или 0 – есть мозг или нет.
Затем период обращения вокруг Солнца.
Количество требуемых дат.
Формат вывода:
Выведите нужное количество ближайших дат безопасного сближения в виде: DD Month YY

Пример 
Ввод:
25.03.2022
1
2
4
Вывод:
31 March 22
06 April 22
12 April 22
18 April

2. Стартовал к Луне ровно в два, сразу после обеда.Похоже простудился в лунной тени - все время чихаю. Принял аспирин. По курсу - три товарные ракеты с Плутона; машинист телеграфировал, что я пропустил их. Спросил, что за груз; думал, бог знает что, а это обыкновенные брындасы.
Напишите программу, создающую несколько различных случайных ракет со случайным грузом на случайных траекториях.
Номер ракеты - прописная буква латинского алфавита из заданного диапазона, две любые цифры, номер целиком не повторяется.
Грузоподъемность - целое число из заданного диапазона с шагом 50, повторения возможны;
Дальность - вещественное число из заданного диапазона с точностью до одного
знака после запятой, без повторений;
Груз - случайная строка из заданного набора, без повторений

Формат ввода: 
Вводится:
Количество ракет,
две буквы латинского алфавита через пробел - диапазон букв для номера, введенные буквы включаются в диапазон;
Два целых числа через пробел - диапазон грузоподъемности;
два вещественных числа через пробел - диапазон дальности;
словосочетания через запятую и пробел - возможные грузы.

Формат вывода: вывести требуемое количество описаний ракет в виде
Rocket<номер>(<грузоподъемность>, <дальность>)follows with cargo of <груз>

Пример:
ввод:
4
S Y
350 1520
9.8 12.6
brundas, sepulchers, crabs, meteorites, asteroids

Вывод:
Rocket W60 (1500, 12.4) follows with cargo of asteroids.
Rocket W17 (1350, 11.8) follows with cargo of bryndas.
Rocket U89 (400, 11.3) follows with cargo of sepulchres.
Rocket T67 (1000, 10.4) follows with cargo of crabs.
Примечания
Подставляемые значения в примере случайны, в задаче не проверяется точное совпадение.
Для вывода вещественного числа с указанным числом знаков можно воспользоваться конструкцией:

a = 3.1
print(f"{a:.2f}")
