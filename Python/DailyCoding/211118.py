# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

class Solution:
    def romanToInt(self, s):
        d = {'M':1000, 'CM':900, 'D':500, 'CD':400, 'C':100, 'XC':90, 'L':50, 'XL':40, 'X':10, 'IX':9, 'V':5, 'IV':4, 'I':1} 

        res = 0
        for c in d:
            length = len(c)
            while c == s[:length]:
                res += d[c]
                s = s[length:]

        return res


sol = Solution()
sol.romanToInt('MMMCCXXXIX')






# class Solution:
# # @param {string} s
# # @return {integer}
#     def romanToInt(self, s):
#         roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
#         z = 0
#         for i in range(0, len(s) - 1):
#             if roman[s[i]] < roman[s[i+1]]:
#                 z -= roman[s[i]]
#             else:
#                 z += roman[s[i]]
#         return z + roman[s[-1]]