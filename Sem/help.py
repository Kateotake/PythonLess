
import re
import itertools


file1 = 'hello1.txt'
file2 = 'hello2.txt'
# file_sum = '34_Sum_polynomials.txt'

# Получение данных из файла

def read_file(file):
    with open(str(file), 'r') as data:
        st = data.read()
    return st
    
st1 = read_file('hello1.txt')
print(st1)
st2 = read_file('hello2.txt')
print(st2)

# Получение списка кортежей каждого (<коэффициент>, <степень>)

def convert_pol(st):
    st = st.replace('= 0', '')
   
    st = re.sub("[*|^| ]", " ", st).split('+')
  
    st = [char.split(' ') for char in st]

    st = [[x for x in list if x] for list in st]

    for i in st:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)

    st = [tuple(int(x) for x in j if x != 'x') for j in st]
    print(st)
    return st
stn1=convert_pol(st1)
stn2=convert_pol(st2)
# Получение списка кортежей суммы (<коэф1 + коэф2>, <степень>)

def fold_pols(st1, st2):   
    x = [0] * (max(st1[0][1], st2[0][1] + 1))
    for i in st1 + st2:        
        x[i[1]] += i[0]
    res = [(x[i], i) for i in range(len(x)) if x[i] != 0]
    res.sort(key = lambda r: r[1], reverse = True)
    print(res)
    return res

fold_pols(stn1,stn2)
# Составление итогового многочлена

# def get_sum_pol(st):
#     var = ['*x^'] * len(st)
#     coefs = [x[0] for x in st]
#     degrees = [x[1] for x in st]
#     new_pol = [[str(a), str(b), str(c)] for a, b, c in (zip(coefs, var, degrees))]
#     for x in new_pol:
#         if x[0] == '0': del (x[0])
#         if x[-1] == '0': del (x[-1], x[-1])
#         if len(x) > 1 and x[0] == '1' and x[1] == '*x^': del (x[0], x[0][0])
#         if len(x) > 1 and x[-1] == '1': 
#             del x[-1]
#             x[-1] = '*x'
#         x.append(' + ')
#     new_pol = list(itertools.chain(*new_pol))
#     new_pol[-1] = ' = 0'
#     return "".join(map(str, new_pol))

# def write_to_file(file, pol):
#     with open(file, 'w') as data:
#         data.write(pol)

# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# pol_1 = convert_pol(pol1)
# pol_2 = convert_pol(pol2)

# pol_sum = get_sum_pol(fold_pols(pol_1, pol_2))
# write_to_file(file_sum, pol_sum)

# print(pol1)
# print(pol2)
# print(pol_sum)