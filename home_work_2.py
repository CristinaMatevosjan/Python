

# Создайте программу для игры в "Крестики-нолики".

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# 1   Напишите программу, удаляющую из текста все слова, содержащие "абв".


text= 'Напиабвшите программу, абв удаляющую из текабвста все слова, содержащие "абв".'
def delete_(text):
    text=list(filter(lambda x: 'абв'not in x, text.split()))
    return " ".join(text)
print(delete_(text))


# 2.    Создайте программу для игры с конфетами человек против человека.

# Условие задачи:
#  На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход, выиграет тот кто сходит последним. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"

#                                     Первая попытка реализации

# from random import randint
# import re

# K=int(input('Введите общее колличество конфет='))
# m=int(input('Введите максимальное колличество изымаемых конфет за 1 ход='))

# def draw():
#     motion=randint(1,2)
#     if motion==1:
#         print('Поздравляю!Победил игрок 1')
#     else:
#         print('Поздравляю!Победил игрок 2')

# def game(K,m):
#     while K>0:
#         right_move=K-(K%(m+1))
#         opponent_move=randint(1,28)
#         remaining_candies=right_move-opponent_move # opponent_move=right_move-(right_move%(m+1))
#         K=remaining_candies
#         if right_move==0:
#             print('Победа!')
#     return draw()  

# game(K,m)     




# Версия 1.1

import random

rules = ('Условие задачи: На столе лежит K конфет.'
'\nИграют два игрока делая ход друг после друга.'
'\nПервый ход определяется жеребьёвкой.'
'\nЗа один ход можно забрать не более чем m конфет.' 
'\nВсе конфеты оппонента достаются сделавшему последний ход,'
'\nвыиграет тот кто сходит последним.'
'\nСколько конфет нужно взять первому игроку,'
'\nчтобы забрать все конфеты у своего конкурента?')

 # man vs man           

messages = ['Ваша очередь брать конфеты', 'Возьмите конфеты', 
            'Сколько конфет возьмёте?', 'Ваш ход']


def play(K, m, players, messages):
    count = 0
    if K%10 == 1 and 9 > K > 10: letter = 'а'
    elif 1 < K%10 < 5 and 9 > K > 10: letter = 'ы'
    else: letter = ''
    while K > 0:
        print(f'{players[count%2]}, {random.choice(messages)}')
        move = int(input())
        if move > K or move > m:
            print(f'Это слишком много, можно взять не более {m} конфет{letter}, у нас всего {K} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if K >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -=1
            else: 
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        K = K - move
        if K > 0: print(f'Осталось {K} конфет{letter}')
        else: print('Все конфеты разобраны.')
        count +=1
    return players[not count%2]

print(rules)

player1 = input('\nДавайте познакомися. Первый игрок, как к Вам можно обращаться?\n')
player2 = input('Второй игрок, и Вы представьтесь, пожалуйста\n')
players = [player1, player2]

K = int(input('Сколько конфет будем разыгрывать?\n '))
m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

winer = play(K, m, players, messages)
if not winer:
    print('У нас нет победителя.')
else: print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

#                       Человек против бота
from random import randint, choice

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
            '\nОсновные правила игры: '
            '\nНам будет дано некоторое количество конфет, '
            '\nза один ход мы можем взять не более определённого количества, '
            '\nо котором мы с вами договоримся. '
            '\nИтак, начнём!\n')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]


print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')






#                      Человек против "умного" бота


from random import randint, choice

greeting = ('Здравствуйте! Вас приветствует игра "Забери все конфеты!" '
            '\nОсновные правила игры: '
            '\nНам будет дано некоторое количество конфет, '
            '\nза один ход мы можем взять не более определённого количества, '
            '\nо котором мы с вами договоримся. '
            '\nИтак, начнём!\n')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']


def introduce_players():
    player1 = input('Давайте познакомися. Как Вас зовут?\n')
    player2 = 'Робик'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]


def get_rules(players):
    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))
    first = int(input(
        f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
    if first != 1:
        first = 0
    return [n, m, int(first)]


def play_game(rules, players, messages):
    count = rules[2]
    print(count)
    if rules[0] % 10 == 1 and 9 > rules[0] > 10:
        letter = 'а'
    elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = rules[0] % rules[1] + 1
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if move > rules[0] or move > rules[1]:
                print(
                    f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[ count % 2]  # ????????


print(greeting)

players = introduce_players()
rules = get_rules(players)

winer = play_game(rules, players, messages)
if not winer:
    print('У нас нет победителя.')
else:
    print(
        f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')