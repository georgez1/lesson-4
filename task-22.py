"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
"""

n = int(input("Введите кол-во чисел в 1-м наборе: "))
array1 = []
for i in range(n):
    a = int(input("Введите целые числа для 1-го набора:"))
    array1.append(a)
m = int(input("Введите кол-во чисел во 2-м наборе: "))
array2 = []
for j in range(m):
    b = int(input("Введите цедые числа для 2-го набора:"))
    array2.append(b)
array3 = []
for i in array1:
    if i in array2 and i not in array3:
        array3.append(i)
array3.sort()
print("1-й набор: {} ".format(array1))
print("2-й набор: {} ".format(array2))
print("Числа в обоих наборах: {} ".format(array3))
