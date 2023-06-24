# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

#import random
#b = random.randint (1, a - 1)

import random
x = random.randint (1, 10)
n = random.randint (5, 10)
c = 0
array = []*n
for i in range(n):
    b = random.randint (1, 10)
    array.append(b)
    if array[i] == x:
        c +=1
print(i+1)
print(" ", *array)
print(" ",x)
print("->", c)
