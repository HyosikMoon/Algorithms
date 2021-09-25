class Solution:
    def longestPalindrome(self, s):
        #initial condition
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        # len(s) >= 2, divide left, right and compare
        w = s[0]
        for i , c in enumerate(s):
            # j, end index of slicing
            j = i + 2
            lim = len(s)

            # from i to j, slice s -> sample
            # compare left and right of the sample
            # repeat until j reach to len(s)
            # O(n^3)
            while j <= lim:
                sample = s[i:j]
                m = len(sample) // 2

                if len(sample) % 2 == 0:
                    l = sample[:m]
                    r = sample[m:]
                    if l == r[::-1] and len(l)*2 > len(w):
                        w = sample
                        j += 1
                        continue
                    j += 1
                else:
                    l = sample[:m]
                    r = sample[m+1:]
                    if l == r[::-1] and len(l)*2 + 1 > len(w):
                        w = sample
                        j += 1
                        continue
                    j += 1
        
        return w

    # O(n^2)
    def longestPalindrome2(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.helper(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    
    # get the longest palindrome, l, r are the middle indexes   
    # from inner to outer
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1; r += 1
        return s[l+1:r]


# sol = Solution()
# sol.longestPalindrome("zdefeeeeeeeeasd")

sol2 = Solution()
sol2.longestPalindrome2("abcba")