class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        prev_err = 1000
        output = (nums[0] + nums[1] + nums[2])
        for left in range(len(nums)-2):
            if left>0 and nums[left] == nums[left-1]:
                left += 1
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                curr_sum = (nums[left] + nums[mid] + nums[right])
                curr_err = abs(curr_sum - target)
                if curr_err < prev_err:
                    output = curr_sum
                    prev_err = curr_err
                if curr_sum < target:
                    while mid < right and nums[mid] == nums[mid+1]:
                        mid += 1
                    mid += 1
                elif curr_sum > target:
                    while mid < right and nums[right] == nums[right-1]:
                        right -= 1
                    right -= 1
                else:
                    break
        return output


            
sol = Solution()
print(sol.threeSumClosest([1,-1,-1,0], 0))