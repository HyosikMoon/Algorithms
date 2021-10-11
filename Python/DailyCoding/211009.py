# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321

class Solution:
    def reverse(self, x):
        sign = 0
        if x < 0:
            sign = 1
        
        if sign == 1:
            x = str(x)[1:]
        else:
            x = str(x)
            
        out = ""
        for c in x:
            out = c + out
        
        if sign == 1:
            out = -1 * int(out)
        else:
            out = int(out)

        if out < -2**31 or out > (2**31 - 1):
            return 0
        else:
            return out
        

    # def reverse(self, x):
    #     """
    #     :type x: int
    #     :rtype: int
    #     """
    #     sign = [1,-1][x < 0]
    #     rst = sign * int(str(abs(x))[::-1])
    #     return rst if -(2**31)-1 < rst < 2**31 else 0