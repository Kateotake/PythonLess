# В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. 
# Найдите это число.


# with open('hello.txt', 'r') as my_file:
#     f = my_file.read().split()
#     f = list(map(int,f))

#     for i in range(len(f)-1):
#         if (f[i]+1) != f[i +1]:
#             print(f[i]+1)






# 1. Дан список чисел. 
# Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
# *Пример:*
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def get_up2(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups
    
print(get_up2(nums))

# Второй вариант

def get_up(nums):
    ups = []
    for i in range(len(nums)):
        if nums[i] == max(nums[:i+1:]) and nums[i] not in ups:
            ups.append(nums[i])
    return ups

print(get_up(nums))




# 38. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв".

# txt = "вап абв пнк апроабв"
# print(txt)

# txt2 = 'абв'
# lst = [i for i in txt.split() if txt2 not in i]
# print(' '.join(lst)) # [вап пнк]


#или

def del_some_words(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_some_words(my_text)
print(my_text)

