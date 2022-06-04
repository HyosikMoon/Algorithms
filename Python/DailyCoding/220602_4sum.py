# class Solution(object):
#   def threeSum(self, nums, target):
#     results = []
#     nums.sort()
#     for i in range(len(nums)-2):
#       l = i + 1; r = len(nums) - 1
#       t = target - nums[i]
#       if i == 0 or nums[i] != nums[i-1]:
#         while l < r:
#           s = nums[l] + nums[r]
#           if s == t:
#             results.append([nums[i], nums[l], nums[r]])
#             while l < r and nums[l] == nums[l+1]: l += 1
#             while l < r and nums[r] == nums[r-1]: r -= 1
#             l += 1; r -=1
#           elif s < t:
#             l += 1
#           else:
#             r -= 1

#     return results

#   def fourSum(self, nums, target):
#     results = []
#     nums.sort()
#     for i in range(len(nums)-3):
#       if i == 0 or nums[i] != nums[i-1]:
#         threeResult = self.threeSum(nums[i+1:], target-nums[i])
#         for item in threeResult:
#           results.append([nums[i]] + item)
#     return results

class Solution:
  def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    results = []
    nums.sort()
    for i in range(len(nums)-3):
      if i != 0 and nums[i] == nums[i-1]:
        continue
      t = target - nums[i]
      result = self.threeSum(nums[i+1:], t)
      # print(result)
      for term in result:
        results.append(term + [nums[i]])
    return results

  def threeSum(self, nums, target):
    results = []
    nums.sort()
    for i in range(len(nums)-2):
      if i != 0 and nums[i] == nums[i-1]:
        continue
      l = i+1; r = len(nums)-1
      while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s == target:
          results.append([nums[i], nums[l], nums[r]])
          while l<r and nums[l] == nums[l+1]: l += 1
          while l<r and nums[r] == nums[r-1]: r -= 1
          l += 1; r -= 1
        elif s < target:
          while l<r and nums[l] == nums[l+1]: l += 1
          l += 1
        else:
          while l<r and nums[r] == nums[r-1]: r -= 1
          r -= 1
    return results

