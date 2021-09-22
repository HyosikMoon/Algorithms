class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums3 = []
        
        # Initial condition
        if len(nums1) == 0 and len(nums2) != 0:
            nums3 = nums2
            if len(nums3) % 2 == 1:
                return nums3[len(nums3)//2]
            else:
                return (nums3[len(nums3)//2] + nums3[len(nums3)//2 - 1]) / 2
        elif len(nums1) != 0 and len(nums2) == 0:
            nums3 = nums1
            if len(nums3) % 2 == 1:
                return nums3[len(nums3)//2]
            else:
                return (nums3[len(nums3)//2] + nums3[len(nums3)//2 - 1]) / 2
        elif len(nums1) == 0 and len(nums2) == 0:
            return 0
        
        # nums3 = sort(nums1 + nums2) 
        for i, num1 in enumerate(nums1):
            if len(nums2) == 0:
                nums3.extend(nums1)
                break
            for j, num2 in enumerate(nums2):
                if num1 >= num2:
                    nums3.append(num2)
                    # nums2.remove(nums2[j])
                    continue
                else:
                    nums3.append(num1)
                    # nums1.remove(nums1[i])
                    break

        # Extend the rest
        if len(nums1) == 0:
            nums3.extend(nums2) 
        
        # Median 
        median = 0
        if len(nums3) % 2 == 1:
            return nums3[len(nums3)//2]
        else:
            return (nums3[len(nums3)//2] + nums3[len(nums3)//2 - 1]) / 2

sol = Solution()
sol.findMedianSortedArrays([1,4], [2,3])