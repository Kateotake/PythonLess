# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".















# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""



# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")








# Создайте программу для игры в ""Крестики-нолики"".

# board = [' ' for el in range(1,10)]
# def print_board(num):
    
#     print("     |     |") 
#     print(f"  {num[0]}  |  {num[1]}  |  {num[2]}") 
#     print('_____|_____|_____') 
#     print("     |     |") 
#     print(f"  {num[3]}  |  {num[4]}  |  {num[5]}") 
#     print('_____|_____|_____') 
#     print("     |     |") 
#     print(f"  {num[6]}  |  {num[7]}  |  {num[8]}") 
#     print("     |     |") 
#     print("") 

# def hod(player, znak):
#     valid = False
#     while not valid:
#         hod = int(input(f'{player}, Ваша очередь ставить {znak} '))
#         if hod in range(10):
#             if board[hod - 1] == ' ':
#                 board[hod-1] = znak
#                 valid = True
#             else:
#                 print('Эта клетка занята, выберете другую')
#         else:
#             print('Такой клетки на поле нет! Необходимо ввести цифру от 1 до 9')

# def win(player, znak):
#     wins= ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#     for el in wins:
#         if board[el[0]] == board[el[1]] == board[el[2]] == znak:
#             print_board(board)
#             print(f'\n{player}, Вы выиграли, поздравляю!')
#             return True
        
#     return False

# def play():
#     raund = 0
#     winn = False
#     while not winn:
#         print_board(board)
#         if raund == 9:
#             print ('У Вас ничья, сыграем еще раз?')
#             break
#         if raund % 2 == 0:
#             hod(player1,'X')
#             if win(player1,'X'):
#                 winn = True
#         else:
#             hod(player2,'O')
#             if win(player2,'O'):
#                 winn = True
#         raund +=1
            

# print('Вас приветствует игра Крестики-Нолики. Игроки, представьтесь пожалуйста!')
# player1 = input('Игрок №1, как Вас зовут?\n')
# player2 = input('Игрок №2, как я могу к Вам обращаться?\n')

# print (f'Приветствую Вас {player1} и {player2}! Давайте сыграем!\n'
# 'Правила просты. \n'
# 'Игроки по очереди ставят на свободные клетки поля 3х3 знаки (крестики или нолики).\n'
# 'Первый, выстроивший в ряд 3 своих фигуры по вертикали, горизонтали или диагонали, выигрывает.')
# print(f'{player1} играет за крестики\n{player2} за нолики\n'
# 'Для того, чтобы поставить совй знак в клетку - напишите цифру, соответствующую этой клетке')

# examp = [el for el in range(1,10)]
# print_board(examp)

# print('Надеюсь, Вам всё ясно! Приступим:')
# play()



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if txt[i].isdigit():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


s = "аааааббсссссссд"
print(f"Текст после кодировки: {coding(s)}")
print(f"Текст после дешифровки: {decoding(coding(s))}")