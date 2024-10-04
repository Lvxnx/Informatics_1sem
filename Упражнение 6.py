def avg(data: list) -> float:
    return (sum(data) / len(data))

x = list(map(int, input().split()))
y = list(map(int, input().split()))
xy = [x[i] * y[i] for i in range(len(x))]
x_sq = [elem ** 2 for elem in x]
b = round((avg(xy) - avg(x) * avg(y)) / (avg(x_sq) - avg(x) ** 2), 3)
a = round(avg(y) - b * avg(x), 3)
print(f'Результат аппроксимации: y = {a} + {b}x')