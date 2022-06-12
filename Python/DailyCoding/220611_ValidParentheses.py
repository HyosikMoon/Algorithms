class Solution:
    def isValid(self, str):
        stack = []
        dict = {'(':')', '[':']', '{':'}'}

        for i in range(len(str)):
            if str[i] in dict.keys():
                stack.append(str[i])
            else:          
                if stack == [] or dict[stack.pop()] != str[i]:
                    return False
        
        return len(stack) == 0