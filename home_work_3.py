# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# Была же такая задача уже?!

# 2. Задайте натуральное число N.
#  Напишите программу, которая составит список простых множителей числа N.

from operator import le
import math


def is_prime(n):
    primes = [2]
    for num in range(3, n + 1, 2):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes


def get_prime_factors(n, primes):
    fact = []
    for i in primes:
        while n % i == 0:
            n = n / i
            fact.append(i)
    return fact

n = int(input('Введите число: '))

primes = is_prime(n)
factors = get_prime_factors(n, primes)
print(factors)


# 3.Реализовать программу, получающую на вход строку,
#  состоящую из слов, разделенных пробелами и возвращающую длину каждого слова. 
# Пример: "Солнце небо воздух земля" --> 6 4 6 5

example_string="Солнце gdfgdg небо воздух dfgjdg земля ghfkjl;;;uh"
len_word=list(map(lambda x: len(x), example_string.split()))
print(len_word)