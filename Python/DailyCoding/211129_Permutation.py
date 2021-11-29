## 1. Arrays and Strings
## 1-2) Permutations

# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s, t):
        d1 = {}
        d2 = {}
        for c in s:
            if c in d1:
                d1[c] += 1
            else:
                d1[c] = 1

        for c in t:
            if c in d2:
                d2[c] += 1
            else:
                d2[c] = 1

        return d1 == d2

sol = Solution()
sol.isAnagram("anagram", "anagram")

    # Solution2.
    # dic1, dic2 = {}, {}
    # for item in s:
    #     dic1[item] = dic1.get(item, 0) + 1
    # for item in t:
    #     dic2[item] = dic2.get(item, 0) + 1
    # return dic1 == dic2

    # Solution3.
    #     return sorted(s) == sorted(t)
