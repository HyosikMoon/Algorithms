class Solution:
    def threeSum(self, nums):

        # Initial condition
        if len(nums) < 3:
            return []

        # Initial setting
        nums.sort()
        output = []

        # Main algorithm
        for left in range(len(nums) - 2):
            # Filter duplicates for left
            if left > 0 and nums[left] == nums[left - 1]:
                continue
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = nums[left] + nums[mid] + nums[right]
                if curr_sum < 0:
                    mid += 1
                elif curr_sum > 0:
                    right -= 1
                else:
                    output.append([nums[left], nums[mid], nums[right]])
                    # Filter duplicates for mid and right
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    while right > mid and nums[right] == nums[right-1]:
                        right -= 1
                    mid += 1
                    right -= 1
        return output

            
sol = Solution()
print(sol.threeSum([1,-1,-1,0]))