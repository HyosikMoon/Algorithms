class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs.sort()
        pre = []

        for a, z in zip(strs[0], strs[-1]):
            if a == z:
                pre.append(a)
            else:
                break
        
        return "".join(pre)

sol = Solution()
print(sol.longestCommonPrefix(['abc', 'abe', 'abpp']))
