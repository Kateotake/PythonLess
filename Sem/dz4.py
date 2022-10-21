# Вычислить число pi c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# Формула Бэйли — Боруэйна — Плаффа

# n = 100
# pi1 = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(pi1)




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
# k=6

# while k > -1:
#     a = random.randint (0,2)
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
# st = st.replace('1*x','x')
# print(st)

# with open("hello.txt", "w") as file:
#     file.write(st)



# from random import randint
# import itertools

# k = 5

# def get_ratios(k):
#     ratios = [randint(0, 2) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(0, 2) 
#     return ratios

# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     print(var)
#     cer = itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') # получается набор символов в массивеб мы три массиве делаем чейн друг между другом 
#     #rations-набор случайных цифр(6 шт(к+1))- [23, 3, 7, 9,45,3]
#     # var []
#     polynomial = [[a, b, c] for a, b, c  in cer if a !=0] # РАЗБИВАЕМ СПИСОКЮ. получается список строк
#     # я знаю что у меня 3 зач абс и сейчас они записаны в один массив. я хочу разделить и получить массив из строк. к примеру [1, с, 2, 3, м, 3, 4, м, 4, 7, м, 8] ----- получится [1c2], [3m3], [4m4], [7m7]
#     # и если а=0 то не делеаем это
#     print(polynomial) 
#     for x in polynomial:
#         x.append(' + ') # если среди элементов есть х, то добавляем к элементу списка +
#     print(polynomial)
#     polynomial = list(itertools.chain(*polynomial)) # СОЕДИНЯЕМ СПИСОК
#     polynomial[-1] = ' = 0' # добавляем в конец =0
#     print(polynomial)
#     polynomial = "".join(map(str, polynomial)) # ДЕЛАЕМ ИЗ СПИСКА ПРОСТО СТРОКУ
#     print(polynomial)
#     polynomial =polynomial.replace(' 1*x',' x') # ЗАМЕНЯЕМ 1Х НА Х
#     print(polynomial)
#     return polynomial


# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
#print(polynom1)


# Второй многочлен для следующей задачи:

#k = 2

#ratios = get_ratios(k) 
#polynom2 = get_polynomial(k, ratios)
#print(polynom2)






# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# # Получение данных из файла

def read_file(file):
    with open(str(file), 'r') as data:
        st = data.read()
    return st

st1 = read_file('hello1.txt')
print(st1)
st2 = read_file('hello2.txt')
print(st2)



# (коэффициент, степень)

def convert_pol(st):
    st = st.replace(' = 0', '') #заменяет 0 на ничего
    st = st.replace('*', ' ')
    st = st.replace('^', ' ')
    st = st.split(' + ')
    st = [char.split() for char in st]
    for i in st:
        if i[0] == 'x': i.insert(0, 1) # добавь на 0ю поз -1
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)

    st = [tuple(int(n) for n in j if n != 'x') for j in st]
    print(st)
    return st

stn1 = convert_pol(st1)
stn2 = convert_pol(st2)

# Сумма значений (коэф1 + коэф2, степень)
lenn =0
if len(stn1) > len(stn2):
    lenn = len(stn1)
else:
    lenn = len(stn2)
st3 = []

st3.append((stn1[0][0]+stn2[0][0], stn1[0][1]))
st3.append((stn1[1][0]+stn2[1][0], stn1[1][1]))
for i in range(len(stn1)):
    for j in range(len(stn2)+1):
        if stn1[i][1] == stn2[j][1]:
                k = stn1[i][0]+stn2[j][0]
                m = stn1[i][1]
                st3 = st3.append((k, m)) 
print(st3)

