"""
Задача 32: Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону (т.е. не
меньше заданного минимума и не больше заданного
максимума)
Пример:
Ввод: [-5, 9, 0, 3, -1, -2, 1,
4, -2, 10, 2, 0, -9, 8, 10, -9,
0, -5, -5, 7] (массив)
Ввод: от  7  до 10 (диапазон) 
Вывод: [1, 9, 13, 14, 19]  (индексы элементов)
"""
from random import randint

def FillArray (arraySize):
    return [randint(-10, 20) for i in range (arraySize)]

len_array = int(input("Введите количество элементов массива: ")) 

array = FillArray(len_array)
print(array)

min_element = int(input("Введите 1-й элемент диапазона: ")) 
max_element = int(input("Введите 2-й элемент диапазона: "))
index = [i for i, j in enumerate(array) if min_element <= j <= max_element]
print(index, sep='\n')



