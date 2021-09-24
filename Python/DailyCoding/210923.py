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

sol = Solution()
sol.longestPalindrome("zdefeeeeeeeeasd")