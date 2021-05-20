# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)


# #  @brief dynamic fibonacci function
# #  @details Use the previous outputs to save runtime
# def fib_dynamic(n):
#     if n < 2:
#         return n

#     f = [0, 1]
#     for _ in range(n-1):
#         f.append(f[-1] + f[-2])

#     return f[-1]


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def fib_dynamic(n):
    fib_value = [0, 1]
    if n < 2:
        return fib_value[n]
    for i in range(2, n + 1):
        fib_value.append(fib_value[i - 2] + fib_value[i - 1])
    return fib_value[n]

print(fib(20), fib_dynamic(20))