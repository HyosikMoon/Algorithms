class ReverseString:
    def reverse_string(self, s):
        if len(s) <= 1:
            return s
        return self.helper(0, len(s) - 1, s)

    def helper(self, start, end, ls):
        if start >= end:
            return
        ls[start], ls[end] = ls[end], ls[start]
        return self.helper(start + 1, end - 1, ls)


# Test #
ls = ['H', 'e', 'l', 'l', 'o']
test = ReverseString()
test.reverse_string(ls)
print(ls)
