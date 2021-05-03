def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


#  @brief dynamic fibonacci function
#  @details Use the previous outputs to save runtime
def fib_dynamic(n):
    if n < 2:
        return n

    f = [0, 1]
    for _ in range(n-1):
        f.append(f[-1] + f[-2])

    return f[-1]
