def digitMul(number: int) -> int:
    num = str(number)
    n = len(num)
    while '0' in num:
        num = num.replace('0','')
    mul = 1
    for c in num:
        mul *= int(c)
    return mul

print(digitMul(123405))