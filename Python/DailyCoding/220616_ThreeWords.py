class Solution:
    def threeWords(self, str):
        lst = str.split()
        cnt = 0
        for w in lst:
            if w[0] in '1234567890':
                cnt = 0; continue
            else:
                cnt += 1
                if cnt >= 3: return True
        return False

sol = Solution()
print(sol.threeWords("Hello World hello"))