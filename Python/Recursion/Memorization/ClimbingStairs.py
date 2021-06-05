def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        
        prev1 = 1
        prev2 = 2
        result = 0
        
        for i in range(3, n + 1):
            result = prev1 + prev2
            prev1 = prev2
            prev2 = result
        return result


        # Method 2.
        # if n <= 2:
        #     return n
        
        # waysList = [0,1,2]
        # for i in range(3, n + 1):
        #     waysList.append(waysList[-1] + waysList[-2])
        
        # return waysList[n]