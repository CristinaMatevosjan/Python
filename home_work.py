#                        Вычислить число Пи c заданной точностью d
# Пример:

# при $d = 0.001, π = 3.141.$ $10^{-10} ≤ d ≤10^{-1}$

# import math

# d=int(input('введите d в диапазоне -10 ≤ d ≤-1: '))
# if -10 <= d <= -1:
#     #print(round(math.pi,-d))
#     print(round(22/7,-d))
      
    
# else:
#     print('неверный диапазон d')


# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.


def Eratosphen(N):

    spisok=[] # тут будут простые числа
    
    for i in range(2,N+1):
        spisok.append(i) 
    num=2 #простое число которое будет проверяться, то есть 2, 3, 5...
    i=0 #для подсчёта(счётчик)

    
    while num < spisok[-1]: #цикл, пока num меньше последнего числа в списке
        while len(spisok) > i: #цикл, пока длина спискa больше i, то естьэто цикл, который проходит по списку в поисках чисел кратных num и удаляет их
            if spisok[i]%num == 0 and spisok[i]!= num: #если остаток от числа в списке на позиции i равен нулю - удаляем из спискa
                
                spisok.pop(i) #удаляем
            i+=1 #проверяем следущую позицию списка
        i=0 #сбрасываем счётчик
 
        #следущее число num
        for j in range(len(spisok)):
            if spisok[j] > num:
                num = spisok[j]
                break
 
    return spisok
prime_numbers=Eratosphen(2**13)#int(input('Введите число, до которого  надо "просеивать" ')))   
 
def Factorization(n):
    prime_factors=[] # здесь будет список простых множителей 
    intermediate_result=[]
    i=0
    while 1 not in intermediate_result:
        while len(prime_numbers)>i:
            if n%prime_numbers[i]==0:
                prime_factors.append(prime_numbers[i])
                
                intermediate_result.append(n//prime_numbers[i])
                
                n=n//prime_numbers[i]
            else:
                i+=1
       
    return prime_factors  
print(Factorization(int(input('Введите число, которое надо разложить = '))))      
