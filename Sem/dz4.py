# Вычислить число pi c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$




# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# n = int(input('Введите число: '))
# lst = []
# for i in range(2, n+1):
#     while n % i == 0:
#         n = n/i
#         lst.append(i)
# print(lst)    



# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# lst = [1, 3, 4, 2, 6, 3, 2, 3]


# for el in lst:
#     if lst.count(el) > 1:
#         lst.remove(el)
# print(lst)

# lst = [1, 3, 4, 2, 6, 3, 2, 3]
# lst2 = []
# for el in lst:
#     if lst.count(el) == 1:
#         lst2.append(el)
# print(lst2)




# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# import random

# st = ''
# k=3

# while k > -1:
#     a = random.randint (0,100)
#     if k == 0:
#         st = st + f'{a} = 0'
#     elif k == 1:
#         st = st + f'{a}*x + '
#     else:
#         st = st + f'{a}*x^{k} + '
#     k -= 1
    
# print(st)

# with open("hello2.txt", "w") as file:
#     file.write(st)



# import random

# st = ''
# k=3

# while k > -1:
#     a = random.randint (0,100)
#     if a != 0:
#         if k == 0:
#             st = st + f' + {a}'
#         elif k == 1:
#             st = st + f'+ {a}*x'
#         else:
#             st = st + f'+ {a}*x^{k} '
#     k -= 1
# st = st + ' = 0'
# st = st[2:]
# print(st)

# with open("hello.txt", "w") as file:
#     file.write(st)



# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open("hello1.txt", "r") as f1:
    lst1 = list(f1.read())
with open("hello2.txt", "r") as f2:
    lst2 = list(f2.read())

print(lst1)
print(lst2)

a = []
b=[]
c=[]
d=[]

for i in range(len(lst1)):
    if lst1[i] == 'x':
        if lst1[i+2] == '3':
            a.append(lst1[i-3])
            a.append(lst1[i-2])
        elif lst1[i+2] == '2':
            b.append(lst1[i-3])
            b.append(lst1[i-2])
        else:
            c.append(lst1[i-3])
            c.append(lst1[i-2])
    if lst1[i] == '=':
        d.append(lst1[i-3])
        d.append(lst1[i-2])





a = str(a)[1:-1].replace(", ", '')
b = str(b)[1:-1].replace(", ", "")
c = str(c)[1:-1].replace(", ", "")
d = str(d)[1:-1].replace(", ")

print(a)
print(b)
print(c)
print(d)
