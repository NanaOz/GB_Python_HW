# Отдал ракету в ремонт. Прошлый раз слишком близко подошел к Солнцу; весь лак облез.
# Завмастерской убеждает купить электрический мозг. У него один есть, вполне приличный,
# почти не бывший в употреблении, мощностью двенадцать паровых душ.
# Напишите программу для определения безопасных дат сближения с Солнцем в зависимости от
# наличия мозга.
# Если мозг есть, то каждое третье сближение безопасное (на двух предыдущих он успевает
# научиться). Если мозга нет, то безопасные только те сближения, что попадают на четверг.
# Формат ввода
# Вводится начальная дата – последнее сближение с Солнцем (не рассматривается как подходящая).
# Затем вводится 1 или 0 – есть мозг или нет.
# Затем период обращения вокруг Солнца.
# Количество требуемых дат.
# Формат вывода
# Выведите нужное количество ближайших дат безопасного сближения в виде: DD Month YY
# Пример 1
# Ввод
# 25.03.2022
# 1
# 2
# 4
# Вывод
# 31 March 22
# 06 April 22
# 12 April 22
# 18 April 22

import datetime as dt

print('ЗАДАНИЕ 1')
day, month, year = map(int, input('Введите дату (dd.mm.yyyy): ').split('.'))
our_date = dt.date(year, month, day)
have_brain = int(input('Введите 0 - если мозга нет. Или 1 - если мозг есть: '))
period = int(input('Введите период обращения вокруг Солнца: '))
numbers_dates = int(input('Введите количество требуемых дат: '))
days_total = dt.timedelta(days=0)
period_days = dt.timedelta(days=period)
count = 0
while count < numbers_dates:
    days_total += period_days
    date_cur = our_date + days_total
    if have_brain and days_total.days % 3 == 0 or not have_brain and date_cur.weekday() == 4 - 1:
        print(date_cur.strftime('%d %B %y'))
        count += 1

# Стартовал к Луне ровно в два, сразу после обеда.
# Похоже простудился в лунной тени - все время чихаю. Принял аспирин.
# По курсу - три товарные ракеты с Плутона; машинист телеграфировал,
# что я пропустил их. Спросил, что за груз; думал, бог знает что,
# а это обыкновенные брындасы.
# Напишите программу, создающую несколько различных случайных ракет со
# случайным грузом на случайных траекториях.
# Номер ракеты - прописная буква латинского алфавита из заданного диапазона,
# две любые цифры, номер целиком не повторяется.
# Грузоподъемность - целое число из заданного диапазона с шагом 50, повторения возможны;
# Дальность - вещественное число из заданного диапазона с точностью до одного
# знака после запятой, без повторений;
# Груз - случайная строка из заданного набора, без повторений
# Формат ввода: Вводится:
# Количество ракет,
# две буквы латинского алфавита через пробел - диапазон букв для номера, введенные буквы включаются в диапазон;
# Два целых числа через пробел - диапазон грузоподъемности;
# два вещественных числа через пробел - диапазон дальности;
# словосочетания через запятую и пробел - возможные грузы.
# Формат вывода: вывести требуемое количество описаний ракет в виде
# Rocket<номер>(<грузоподъемность>, <дальность>)follows with cargo of <груз>
# Пример:
# ввод:
# 4
# S Y
# 350 1520
# 9.8 12.6
# brundas, sepulchers, crabs, meteorites, asteroids
# Вывод:
# Rocket W60 (1500, 12.4) follows with cargo of asteroids.
# Rocket W17 (1350, 11.8) follows with cargo of bryndas.
# Rocket U89 (400, 11.3) follows with cargo of sepulchres.
# Rocket T67 (1000, 10.4) follows with cargo of crabs.
# Примечания
# Подставляемые значения в примере случайны, в задаче не проверяется точное совпадение.
# Для вывода вещественного числа с указанным числом знаков можно воспользоваться конструкцией:
#
# a = 3.1
# print(f"{a:.2f}")

import random

print('ЗАДАНИЕ 2')
number_missiles = int(input('Введите количество ракет: '))
range_of_letters_for_number = input('Введите две буквы латинского алфавита '
                                    'через пробел (диапазон букв для номера):'
                                    ' ').split()
load_capacity_range = list(map(int, input('Введите два целых числа через '
                                          'пробел (диапазон '
                                          'грузоподъемности): ').split()))
range_of_distance = list(map(float, input('Введите два вещественных числа '
                                          'через пробел (диапазон дальности):'
                                          ' ').split()))
possible_loads = input('Введите возможные грузы (словосочетания через '
                       'запятую и пробел ): ').split(', ')


def rand_letter(x, y):
    return chr(random.randint(ord(x), ord(y)))


def rand_num(x, y):
    return random.randint(x, y)


for i in range(number_missiles):
    num_char = rand_letter(range_of_letters_for_number[0],
                           range_of_letters_for_number[1])
    num = rand_num(10, 100)
    load_capacity = random.randrange(load_capacity_range[0],
                                     load_capacity_range[1], 50)
    range_dis = random.uniform(range_of_distance[0], range_of_distance[1])
    cargo = possible_loads[random.randint(0, len(possible_loads) - 1)]
    print(
        f'Rocket {num_char}{num}({load_capacity}, {range_dis:.1f}) follows '
        f'with cargo of {cargo}')
