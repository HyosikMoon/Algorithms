from re import I


class Solution:
    def beginning_zeros(self, number):
        num = 0
        for i, c in enumerate(number):
            if number[i] == str(0):
                print(i, c)
                num += 1
            else:
                break
        return num
sol = Solution()
sol.beginning_zeros('002')