def factorize(n):
    f = []
    while n % 2 == 0:
        n //= 2
        f.append(2)
    i = 3
    while n != 1:
        while n % i == 0:
            n //= i
            f.append(i)
        i += 2
    return f

n = int(input())
print(*factorize(n))