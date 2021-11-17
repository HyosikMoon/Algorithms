# For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given an integer, convert it to a roman numeral.


class Solution:
    # def intToRoman(self, num):
    #     # step1. 10^3 = ?, 10^2, 10^1, 10^0 => ?
    #     # step2. 7 symbols (1,5,10,50,100,500,1000)
    #     #                 - I, V, X, L, C, D, M
    #     # step3. exception -> 4, 9, 40, 90, 400, 900
    #     #                  - IV, IX, XL, XC, CD, CM
    #     # step4. How to combine them?

    #     # 10^3 -> num * M
    #     # 10^2 -> C CC CCC CD D DC DCC DCCC CM
    #     # 10^1 -> X XX XXX XL L LX LXX LXXX XC
    #     # 10^0 -> I II III IV V VI VII VIII IX

    #     # Make tables
    #     dicts = {3000:"MMM", 2000:"MM", 1000:"M", 900:"CM", 800:"DCCC", 700:"DCC", 600:"DC", 500:"D", 400:"CD", 300:"CCC", 200:"CC", 100:"C", 
    #             90:"XC", 80:"LXXX", 70:"LXX", 60:"LX", 50:"L", 40:"XL", 30:"XXX", 20:"XX", 10:"X",
    #             9:"IX", 8:"VIII", 7:"VII", 6:"VI", 5:"V", 4:"IV", 3:"III", 2:"II", 1:"I"}

    #     # Setting
    #     output = ""
    #     denominator = 1000
    #     digit = 1000
    #     values = []

    #     # Extract digit values
    #     while (denominator >= 1):
    #         values.append(num//denominator)
    #         num = num % denominator
    #         denominator = denominator//10
        

    #     while values != []:
    #         value = values[0]*digit
    #         digit = digit//10
    #         values.remove(values[0])
    #         if value == 0:
    #             continue
    #         else:
    #             output = output + dicts[value]

    #     return output


# Sample solution.
# class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'} 
        
        res = ""

        for i in d:
            res += (num//i) * d[i]
            num %= i

        return res




sol = Solution()
sol.intToRoman(2379)