# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums):
        d = []
        length = len(nums)
        while length != 0:
            elem = nums.pop()
            if elem in nums:
                return True
            length -= 1
        return False


        # d = []
        # for e in nums:
        #     if e in d:
        #         return True
        #     else:
        #         d.append(e)
        # return False


sol = Solution()
sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2])