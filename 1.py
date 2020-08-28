# первое задание
# x = 8
# y = 7.3
# print('Переменные числа x & y - ', x, y)
# first_string = input('Быстрее печатай буквы ')
# first_number = int(input('Реще вбивай числа '))
# print('Что напеатали твои корявки - %10s %5d'  % (first_string, first_number))

# третье задание
# n = int(input('Каким чеслом запряжёшь? - '))
# total = (n + int(str(n) + str(n)) + int(str(n) + str(n)+ str(n)))
# print('Эх сейчас посчитаю n + nn + nnn - %d' % total)

# # четвёртое задание
# n = abs(int(input('число без дробей и минусов ')))
# max = n % 10
# while n >= 1:
#     n = n // 10
#     if n % 10 > max:
#         max = n % 10
#     if n > 9:
#         continue
#     else:
#         print('наибольшая циферка в числе ', max)
#         break

# # шестое задание
# km_1 = int(input('Пробегал в первый день '))
# km_2 = int(input('Сколько хочешь бегать в день за молоком   '))
# result_days = 1
# result_km = km_1
# while result_km < km_2:
#         km_1 = km_1 + 0.1 * km_1
#         result_days += 1
#         result_km = result_km + km_1
# print(f'Будешь кртуым побегушником на %.d день' % result_days)

# третье задание
# time = int(input('Ну какое время посчитать по секундам, голову напрягать этим заданием, пиши в секундах '))
# hours = time // 3600
# minutes = (time - hours * 3600) // 60
# seconds = time - (hours * 3600 + minutes * 60)
# print(f'Время чётко по формату чч:мм:сс   {hours} : {minutes} : {seconds}')

# пятое задание
# profit = float(input('сколько бабла состригли ' ))
# costs = float(input('сколько бабок ушло на дело '))
# if profit > costs:
#     print(f'Фирма рубит бабки. Накосили за месяц {profit / costs:.2f}')
#     workers = int(input('Сколько работает рабов у нас '))
#     print(f'один раб зарабатывает фирме {profit / workers:.2f}')
# elif profit == costs:
#     print('По бабкам стоим на месте надо, перестать кормить рабов')
# else:
#     print('Теряем бабосы')