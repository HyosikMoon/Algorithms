class Solution(object):
    def letterCombinations(self, digits):
    #     """
    #     :type digits: str
    #     :rtype: List[str]
    #     """
    #     if len(digits) ==0:
    #         return []

    #     dict = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
    #     res=[]
            
    #     self.dfs(digits, 0, dict, '', res)
    #     return res
    
    # def dfs(self, digits, index, dict, path, res):
    #     if index >= len(digits):
    #         res.append(path)
    #         return
    #     strings = dict[digits[index]]
    #     for char in strings:
    #         self.dfs(digits, index+1, dict, path + char, res)

        dict = {'2':'abc', '3':'def', "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []

        if len(digits) == 0:
            return []
        
        self.dfs(digits, 0, dict, '', res)
        return res

    def dfs(self, digits, index, dict, path, res):
        if index >= len(digits):
            res.append(path)
            return

        str = dict[digits[index]]
        for char in str:
            self.dfs(digits, index+1, dict, path+char, res) 

sol = Solution()
print(sol.letterCombinations('23'))