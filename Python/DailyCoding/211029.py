#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

#Notice that you may not slant the container.

class Solution:
    # Solution 1. O(n!) 
    # def maxArea(self, height):
    #     # Find the max area
    #     # area_height =  min(y1=height[i1], y2=height[i2]), length = i2 - i1
        
    #     area = 0
    #     for i, y1 in enumerate(height):
    #         for j, y2 in enumerate(height[i+1:]):
    #             area_length = (j+1)
    #             area_height = min(y2, y1)
    #             sub_area = area_length * area_height
    #             if sub_area > area:
    #                 area = sub_area

    #     return area

    # Solution 2. From the end x -> until find the same heigh[x]
    def maxArea(self, height):
        # Find the max area
        # Make a dictionary of heights according to indices. 
        # Find the min height and its index
        # -> Find the farthest index and height
        # -> distance from two indices is the lenght, and the min height is the height of the area
        # -> That is the biggest area of the index
        # -> Delete the index one by one.
        
        # area = 0
        # reverse_height = height[::-1]
        # length = len(height)
        # for i, y1 in enumerate(height):
        #     for j, y2 in enumerate(reverse_height):
        #         area_height = min(y1,y2)
        #         if (i+j != length and y1 <= y2):
        #             area_length = length - (i+j)
        #             sub_area = area_length * y1
        #             if sub_area > area:
        #                 area = sub_area
        #                 break
        #         else:
        #             continue


        # return area

    # def maxArea(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #     MAX = 0 
    #     x = len(height) - 1
    #     y = 0
    #     while x != y:
    #         if height[x] > height[y]:
    #             area = height[y] * (x - y)
    #             y += 1
    #         else:
    #             area = height[x] * (x - y)
    #             x -= 1
    #         MAX = max(MAX, area)
    #     return MAX

sol = Solution()
sol.maxArea([1,8,6,2,5,4,8,3,7])