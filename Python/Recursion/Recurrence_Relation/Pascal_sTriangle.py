class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Base case
        a = [[1], [1, 1]]
        if rowIndex < 2:
            return a[rowIndex]

        row = 2
        for row in range(row, rowIndex + 1):
            add = [1]
            i = 0
            while i < row - 1:
                add.append(a[row - 1][i] + a[row - 1][i + 1])
                i += 1
            add.append(1)
            a.append(add)
        return a[rowIndex]

# class Solution:
#     def getRow(self, rowIndex: int): # -> List[int]:
#         row = [1]
#         for i in range(rowIndex):
#             for j in range(i, 0, -1):
#                 row[j] = row[j] + row[j-1]
#             row.append(1)
#         return row

Solution().getRow(3)