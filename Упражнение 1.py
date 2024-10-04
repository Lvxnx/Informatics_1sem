def fib(n):
    dp = [0, 1] + [None] * n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

n = int(input())
print(fib(n))