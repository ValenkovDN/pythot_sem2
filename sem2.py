#Задача №14. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.
# n = input('Введите число: ')
# sum = 0
# for i in n:
#     if i != '.':
#         sum += int(i)
# print(sum)

#Задача №15. Напишите программу, которая принимает на вход число N и 
#выдает набор произведений чисел от 1 до N.
# n = int(input('Введите число: '))
# m = 1
# list = []
# for i in range(1,n+1):
#     m = m * i
#     list.append(m)
# print(list)

#Задача №16. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и 
# выведите на экран их сумму.
# n = int((input('Введите число: ' )))
# list = []
# sum = 0
# for i in range(1,n+1):
#     list.append(round((1+1/i)**i, 2))
#     sum += round((1+1/i)**i, 2)
# print(list)
# print(sum)

#Задача №18. Реализуйте алгоритм перемешивания списка.
# list = []
# import random
# for i in range(int(input('введите длину списка '))):
#     list.append(input('введите данные '))
# print(list)
# random.shuffle(list)
# print(list)