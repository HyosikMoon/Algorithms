class Solution:
    def lengthOfLongestSubstring(self, s):
        
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1

        d = {}
        limit = len(s)

        for i, c in enumerate(s):
            j = i
            w = ''

            # from j to non-repeat substring
            # save length of the substring
            while j <= limit - 1:
                if s[j] not in w:
                    w += s[j]
                    j += 1
                else:
                    d[w] = len(w)
                    break
            d[w] = len(w)
            
        return max(d.values())

sol = Solution()
sol.lengthOfLongestSubstring('au') 


# class Solution:
#     # @return an integer
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
        
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)

#             usedChar[s[i]] = i

#         return maxLength