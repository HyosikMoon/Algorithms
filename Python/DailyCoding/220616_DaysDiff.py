from datetime import date, timedelta

class Solution:
    def days_diff(self, a, b):
        a = date(*a)
        b = date(*b)
        return (a-b).days if a>b else (b-a).days

sol = Solution()
print(sol.days_diff((1982, 4, 19), (1982, 4, 22)))