import sys

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # if x == 0:
        #     return 0
        # if n == 0 or x == 1:
        #     return 1

        # m = n // 2
        # out = 1.0
        # while m != 0:
        #     if m > 0:
        #         out = out * x
        #         m -= 1
        #     else:
        #         out = out * 1.0 / x
        #         m += 1
        # if n % 2 == 0:
        #     return out * out
        # elif n > 0:
        #     return x * out * out
        # else:
        #     return x * out * out


        if n == 0:
            return 1    
        if n == 1:
            return x
        if n == -1:
            return 1/x

        half = self.myPow(x, n/2)
        if n % 2 == 0:
            return half * half
        return x * half * half


Solution().myPow(8.84372, -5)


## Solution 1
#         return x**n


## Solution 2
#         if n == 0:
#             return 1
#         elif n < 0:
#             return 1 / x * self.myPow(x, n + 1)
#         else:
#             return x * self.myPow(x, n - 1)


## Solution 3
#         if n == 0:
#             return 1    
#         if n == 1:
#             return x
#         if n == -1:
#             return 1/x

#         half = self.myPow(x, n/2)
#         if n & 1 == 0:
#             return half * half
#         return x * half * half