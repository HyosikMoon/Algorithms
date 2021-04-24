def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

## @brief dynamic fibonacci function
#  @details Use the previous outputs to save runtime
def fib_dynamic(n):
    if