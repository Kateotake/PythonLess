# созадем словарь 3n+1

# my_dict = {}
# n = 6
# for i in range(1, n+1):
#     my_dict[i] = 3*i + i
# print(my_dict)

# 1. Реализуйте алгоритм задания случайных чисел 
# без использования встроенного генератора псевдослучайных чисел.

# a = 134579

# my_list = []
# for i in range(10):
#     n = a%100
#     my_list.append(n)
#     a = (a *34573525243) %100000

# print(my_list)




# 2. Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число.


# el = [123, '567', '634', 35]

# def check(n,el):
#     for e in el:
#         if e == n:
#             return True
#     return False

# if check(123,el):
#     print('yes')
# else:
#     print('no')


# 3. Напишите программу, которая определит позицию 
# второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1





lst = [2, 6, 7, 9, 4, 8, 9, 3, 2, 6]

# for i in range(len(lst)):
#     if flst == lst[i]:
#         cunt +=1
#         if cunt == 2:
#             print(i)
# if cunt < 2:
#     print('no')

# можно через ретерн


def duuu(lst,str):
    if lst.count(str) < 2:
        return -1
    i1 = lst.index(str)
    i2 = lst. index(str,i1+1)
    return i2

print(duuu(lst,9))

