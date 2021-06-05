def fib(N):
    if N < 2:
        return N
    return fib(N - 1) + fib(N - 2)


def fib_memorization(N):
    ls = [0, 1]
    if N < 2:
        return ls[N]
    
    for i in range(2, N + 1):
        ls.append(ls[i - 1] + ls[i - 2])
    
    return ls[N]


def fib_saveMemory(n):
    if n < 1:
        return n
    
    if n == 2:
        return 1

    result = 0
    prev1 = 1
    prev2 = 1

    for i in range(3, n + 1):
        result = prev1 + prev2
        prev1 = prev2
        prev2 = result
    return result


# Test #
print(fib(15))
print(fib_memorization(15))
print(fib_saveMemory(15))