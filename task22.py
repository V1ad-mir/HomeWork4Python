# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
from random import randint


def filling(elements_set):
    my_list = []
    set_ = {}
    while (len(set_)) < elements_set:
        my_list.append(random.randint(-10, 100))
        set_ = set(my_list)
    return set_


elements_set1 = int(input('Введите количество элементов первого множества: '))
elements_set2 = int(input('Введите количество элементов второго множества: '))
set_1 = filling(elements_set1)
set_2 = filling(elements_set2)
set_intersection = set_1.intersection(set_2)

print(set_1)
print(set_2)
print(sorted(set_intersection))


