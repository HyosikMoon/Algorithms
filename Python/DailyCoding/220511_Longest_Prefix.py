class Solution:
    def longestCommonPrefix(self, strs) -> str:
## Solution 1.2
        strs.sort()
        pre = ""

        for a, z in zip(strs[0], strs[-1]):
            if a == z:
                pre += a
            else:
                break
        
        return pre

# sol = Solution()
# print(sol.longestCommonPrefix(["dog","racecar","car"]))
sol = Solution()
print(sol.longestCommonPrefix(['abc', 'abe', 'abpp']))

## Solution 1.
#         strs.sort()
#         pre = []

#         for a, z in zip(strs[0], strs[-1]):
#             if a == z:
#                 pre.append(a)
#             else:
#                 break
        
#         return "".join(pre)

# sol = Solution()
# print(sol.longestCommonPrefix(['abc', 'abe', 'abpp']))


## Solution 2.
#         # initial condition
#         if len(strs) == 1:
#             return strs[0]

#         strs.sort()
#         min = len(strs[0])
#         if len(strs[0]) > len(strs[-1]):
#             min = len(strs[-1])

#         output = ""
#         for i in range(min):
#             if strs[0][i] == strs[-1][i]:
#                 output += (strs[0][i])
#             else:
#                 break

#         return output

# sol = Solution()
# print(sol.longestCommonPrefix(["dog","racecar","car"]))

