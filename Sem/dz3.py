# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# def summ_un(lst):

#     sum = 0
#     for i in range(len(lst)):
#         if (i % 2 == 1):
#             sum = sum + lst[i]
#     return sum

# num = list(map(int, input('Введите значения через пробел: ').split()))
# print(num)
# print(f'Сумма элементов, стоящих на нечётных позициях - {summ_un(num)}')




# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# import math

# def prod_el(lst):
#     lst2 = []
#     for i in range(math.ceil(len(lst)/2)):

#         lst2.append(lst[i] * lst[-i-1])
#         i +=1
#     return lst2

# num = list(map(int, input('Введите значения через пробел: ').split()))
# print(num)
# print(prod_el(num))




# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# lst = [1.1, -1.2, 3.1, 5, 10.01]
# lst2 =[]

# for item in lst:
#     item = round(item)
#     lst2.append(item) # создаю новый список из целых значений элементов

# lst3 =[]
# for i in range(len(lst)):
#     i = abs(lst[i] - lst2[i]) # abs - если вдруг число будет отрицательным
#     if i != 0:
#         lst3.append(i) # создаю новый список где оставляю только дробную часть(без нуля)
# lst3.sort() # сортирую дробные части

# print(f'Разница между макс и мин значениями дробных частей равна {round((lst3[-1] - lst3[0]),2)}')



# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# N = int(input('Введите десятичное число: '))
# lst = []
# while N != 0:
#     lst.append(int(N % 2))
#     N = N // 2 
# lst.reverse()

# print("".join(map(str,lst))) 


# N = int(input('Введите десятичное число: '))
# st = ''
# while N!= 0:
#     st = str(N % 2) + st
#     N = N // 2
# print(st)



# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


# сначала делаю отрицательную последовательность и переворачиваю ее
# N = int(input('Введите число: '))
# f=[0,1]

# for i in range(2, N+1):
#     f1 = f[i-2] - f[i-1]
#     f.append(f1)
# f.reverse() 

# # потом делаю положительную последовательность 
# ff = [0,1]

# for i in range(2, N+1):
#     f2 = ff[i-1] + ff[i-2]
#     ff.append(f2)
# ff.remove(0) #удаляю 0
# f.extend(ff) # соединяю два списка
# print(f)