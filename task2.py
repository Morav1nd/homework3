import random
x = random.randint (1, 100)
Range = random.randint (5, 10)
array = []*Range
for i in range(Range):
    a = random.randint (1, 100)
    array.append(a)
array.append(x)
array = sorted(array)
print(array)

print(f"число х={x}")


b = array.index(x) + 1
b = array[b]
print(f"следующее число {b}")
difference1 = b - x

c = array.index(x) - 1
c = array[c]
print(f"предидущее число {c}")
difference2 = x - c


if difference1 > difference2:
    print(f"самое близкое по значению {c}")
else:
    print(f"самое близкое по значению {b}")