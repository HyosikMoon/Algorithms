# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 
class Solution:
    # def convert(self, s, numRows):
        # while r < len(s):
        #   a = ['','', ... ,'',''] // an
        #   a0, a1, ... , a_(n-1), a_(n-2), ... , 
        #   s[0], s[1], ... s[n-1], s[n-2], s[n-3], ... , s[0]
        #   a0 ++ a1 ++ ... ++ an
        # 
        # 




# class Solution2(object):
    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)