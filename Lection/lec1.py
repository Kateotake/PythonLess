# print('hello')
#______________________________________________
# типы данных и переменные
# int, float, boolean, str, list, None

# val = None  # если надо присвоить неизвестное значение переменной
# f = 123
# b = 1.23
# print(type(f))
# print(type(b))
# val = 12345
# print(type(val))
# s = "hello world" # строка - одинарные или двойные кавычки
# n = 'hi \'there' # \' если надо внутри строки написать апостроф
# d = 'hi \nthere' # \n - перенос строки


# print(s, '-', n, '--', b) #можно писать при выводе любой текст и переменные

# print(f'{f} - {b} - {s}')
# print('{1} - {2} - {0}'.format(f, b, s))

#__________________________________________
# булевы переменные
# f = True
# print(f)

#__________________________________________
# массивы
# list = [1, 2, 3, 'hello', 2.3, True]
# print(list)

#__________________________________________
# ввод и вывод данных
# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, '+', b, '=', a + b) # если написать так, то сумма а и б будет не 10+20=30, а 10+20 = 1020. 
#Потому что по умолчанию из инпута берется строка
# если нужно целое число взять из строки, то:
# print('Введите s')
# s = int(input()) # или float если надо дробное число
# print('Введите d')
# d = int(input())
# print (s,'+', d, '=', s+d)


#____________________________________________________________
# арифметические операции
# +, -, *, /, %, //, **
# (), сокращенные операции

# a = 2
# b = 8
# c = a / b # питон автоматически поделит  в формате вещ.чисел с запятой
# d = a // b # если надо без запятой, в целых числах
# f = a ** b # возведение в степень
# print(c)
# print(d)
# print(f)

# a = 1.3
# b = 3
# q = a*b # если умножить вещ.число на целое, то получится не 3.9, а 3.900000000000000000004.
# # чтобы этого избежать, надо округлять
# c = round(a*b) # округление до целого
# h = round(a*b,5) # округление до 5 знаков
# b += 5 # то же самое b = b + 5
# b *= 5 # то же самое b = b * 5

#___________________________________________________
# логические операции
# >, >=, <, <=, ==, !=
# not, and, or не путать с &, |. ^
# кое-что еще: is, is not, in, not in
# gen

# a = 1 < 4 and 5 > 2  # true
# b = 1 ==2 # false
# c = 1!=2 # true

# n = 'qwe'
# m = 'qwe'
# print (n == m) # true. Можно сравнивать сроки

# r = [1,2]
# l = [1,2]
# print(r == l) #true. Можно сравнивать списки(массивы)

# Можно сравнивать сройные и четверные выражения типа
# h = 1 < 3 < 4 < 6 # будет true


#____________________________________________________
# логические операции or, and, not 


# f = 1 > 2 or 4 < 6 
# print(f) # будет true . OR - выражение истина, если хотя бы одно из его чатсей истина
# k = [1, 2, 3, 4]
# print(2 in k) # будет true. 2 есть в массиве
# print(not 2 in k) # будет false. 2 есть в массиве

# is_odd = k[0] % 2 == 0
# is_odd1 = not k[0] % 2 # то же самое что и сверху выражение
# print(is_odd) # будет false . остаток от деления 1 на 2 - 1 не равно 0


#_____________________________________________________________
# if, if-else

# a = int(input('a = ')) # в строке сразу выведется a=
# b = int(input('b = '))
# if a>b:
#     print(a)
# else:
#     print(b)

# также есть операторы elif, если много переменных

#______________________________________________________________
# while и while-else, for

# orig = 23
# inv = 0
# while orig !=0:
#     inv = inv * 10 + (orig % 10)
#     orig //= 10
# else:
#     print ('Пожалуй \nХватит')
# print(inv)


# for i in [1, 2, 3, 4, 6]:
#     print(i**2)

# list = [1,6,4]
# for j in list:
#     print(j) # то же самое что и сверху

# list2 = range(10)
# for i in list2:
#     print(i) # выведет цифры от 0 до 9

# for i in range(10):
#     print(i) #то же самое что и сверху

# for i in range(1,10):
#     print(i) # выведет цифры от 1 до 9

# for i in range(1,10,2):
#     print(i) # выведет цифры от 1 до 9 С ШАГОМ 2!

# for i in 'qwerty':
#     print(i) # переберет строку с точностью до пробелом

#___________________________________________________________
# строки

# text = 'съешь еще этих мягких французских булок'
# print(len(text)) #39 - длина строки
# print('еще' in text) #true - есть ли слово еще в текстк
# print(text.isdigit()) #false - явл.ли все симв. числами
# print(text.islower()) #true - явл. ли все симв - симв нижнего регистра
# print(text.replace('еще', 'ЕЩЕ')) # заменим слова

# # если что-то не ясно можно написать help() и дадут подсказку

# # можно образаться к строке как к массиву символов
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)]) # выдаст ошибку тк индексация с нуля
# print(text[len(text)-1]) # к
# print(text[-5]) # б - с конца
# print(text[:]) # print(text) - по умолчанию будет от 0 до len.text -1
# print(text[:2]) # съ - от 0 до 2
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

#_______________________________________________________________
# списки

# numbers = [1, 2, 3, 4, 5]
# print(numbers) # [1, 2, 3, 4, 5]
# numbers = list(range(1, 6)) # range - это строка
# print(numbers) # [1, 2, 3, 4, 5]
# numbers[0] = 10
# print(numbers) # [10, 2, 3, 4, 5]
# for i in numbers:
#     i *= 2
#     print(i) # [20, 4, 6, 8, 10]
# print(numbers) # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e) # red green blue
# for e in colors:
#     print(e*2) # redred greengreen blueblue
# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент

#________________________________________________________________
# функции

# def function_name(x):
# body line 1
# . . .
# body line n
 # optional return

# def f(x):
#     return x**2

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# print(f(1)) # Целое
# print(f(2.3)) # 23
# print(f(28)) # None
# print(type(f(1))) # str
# print(type(f(2.3))) # int
# print(type(f(28))) # NoneType