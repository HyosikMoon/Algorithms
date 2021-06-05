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