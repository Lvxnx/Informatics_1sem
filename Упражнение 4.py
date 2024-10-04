def triangle(size, symb):
    data = []
    for i in range(1, size // 2 + 1 + (size % 2 != 0)):
        data.append(symb * i)
    data += data[-(1 + (size % 2 != 0))::-1]
    for elem in data:
        print(elem)

a, b = input().split()
a = int(a)
triangle(a, b)
