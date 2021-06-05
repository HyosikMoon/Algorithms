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

# Test #
print(fib(15))
print(fib_memorization(15))
print(fib_saveMemory(15))