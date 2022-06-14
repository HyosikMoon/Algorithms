class Solution:
    def max_digit(self, number):
        # your code here
        if len(str(number)) <= 1:
            return number
        else:
            itr = len(str(number))
            num = str(number)
            max = int(num[0])
            for i in range(itr):
                temp = int(num[i])
                if max < temp: max = temp
        return max
sol = Solution()
assert sol.max_digit(52) == 5