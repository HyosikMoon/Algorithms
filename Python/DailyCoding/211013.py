# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x):
        # initial condition
        if x < 0:
            return False
        x = str(x)
        if len(x) <= 1:
            return True

        if len(x)%2 == 1:
            c = len(x)//2
            i = 0
            while (c-i >= 0 and c+i < len(x)):
                if x[c-i] != x[c+i]:
                    return False
                i += 1
            return True
        else:
            s = 0
            e = -1
            i = 0
            while (i < len(x)//2):
                if x[s+i] != x[e-i]:
                    return False
                i += 1
            return True

#Solution1
        # if x < 0:
        #     return False
        
        # return str(x) == str(x)[::-1]


            
#Solution2
        # if x<0:
        #     return False
        # inputNum = x
        # newNum = 0
        # while x>0:
        #     newNum = newNum * 10 + x%10
        #     x = x//10
        # return newNum == inputNum