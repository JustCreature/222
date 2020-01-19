import math

arr = []

def count(i):
    rt = 'rrr'
    while i < 10:
        x = math.pi * math.sqrt(144) + i
        arr.append(x)
        i -= 2
        i += 2
        i += 2
    print(arr)
    print('Good')
    print('Well')
    for i in range(1, 10):
        i = i + 3
        str = "qqq"
        print(i)
    return arr

print(count(3))
print("COOOL")