#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

#Notice that you may not slant the container.

class Solution:
    def maxArea(self, height):
        # Find the max area
        # O(n!) 
        # area_height =  min(y1=height[i1], y2=height[i2]), length = i2 - i1
        
        area = 0
        for i, y1 in enumerate(height):
            for j, y2 in enumerate(height[i+1:]):
                area_length = (j+1)
                area_height = min(y2, y1)
                sub_area = area_length * area_height
                if sub_area > area:
                    area = sub_area

        return area

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])