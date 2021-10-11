# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.


# https://www.w3schools.com/python/python_regex.asp
# https://leetcode.com/problems/string-to-integer-atoi/discuss/4653/Python-solution-based-on-RegEx
class Solution:
    def myAtoi(self, s):
        digit = "0123456789"
        start = 0
        end = 0
        sign = 1

        # Initial condition
        if len(s) == 0:
            return 0
        elif s == " ":
            return 0
        elif s == "-":
            return 0
        elif s == "+":
            return 0
        elif "+-" in s or "-+" in s:
            return 0

        for i, c in enumerate(s):
            if c != '+' and c != ' ' \
                and c != '-' and c not in digit:
                return 0
            elif c in digit:
                start = i
                break
            else:
                continue

        revIndex = -1
        n = 0
        while n < len(s):
            c = s[revIndex]
            if c in digit:
                end = revIndex
                break
            revIndex -= 1
            n += 1

        # Check the sign
        if start > 0 and s[start-1] == '-':
            sign = -1

        # Remove initial 0s
        while s[start] == '0':
            start += 1

        nlmt = -2**31
        plmt = 2**31 - 1
        if end == -1:
            out = sign * float(s[start:])
            if out < nlmt:
                out = nlmt
            elif out > plmt:
                out = plmt
            else:
                return round(out)
        else:
            out = sign * float(s[start:end+1])
            if out < nlmt:
                out = nlmt
            elif out > plmt:
                out = plmt
            else:
                return round(out)
        return round(out)
sol = Solution()
sol.myAtoi("+1")


# Solution
    # def atoi(self, str):
    #     str = str.strip()
    #     str = re.findall('(^[\+\-0]*\d+)\D*', str)

    #     try:
    #         result = int(''.join(str))
    #         MAX_INT = 2147483647
    #         MIN_INT = -2147483648
    #         if result > MAX_INT > 0:
    #             return MAX_INT
    #         elif result < MIN_INT < 0:
    #             return MIN_INT
    #         else:
    #             return result
    #     except:
    #         return 0