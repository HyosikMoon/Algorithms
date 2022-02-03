# https://practice.geeksforgeeks.org/problems/merge-sort/1/
# Given an array arr[], its starting position l and its ending position r. Sort the array using merge sort algorithm.
# Example 1:

# Input:
# N = 5
# arr[] = {4 1 3 9 7}
# Output:
# 1 3 4 7 9
# Example 2:

# Input:
# N = 10
# arr[] = {10 9 8 7 6 5 4 3 2 1}
# Output:
# 1 2 3 4 5 6 7 8 9 10

# Your Task:
# You don't need to take the input or print anything. Your task is to complete the function merge() which takes arr[], l, m, r as its input parameters and modifies arr[] in-place such that it is sorted from position l to position r, and function mergeSort() which uses merge() to sort the array in ascending order using merge sort algorithm.

# Expected Time Complexity: O(nlogn) 
# Expected Auxiliary Space: O(n)

# Constraints:
# 1 <= N <= 105
# 1 <= arr[i] <= 103

# class Solution:
#     def merge(self, arr, l, m, r):
#         if len(arr) == 1:
#             return 0
#         il = l
#         k, z1, z2 = 0, 0, 0
#         ir = m+1
#         comp1 = arr[l]
#         comp2 = arr[m+1]
#         while(il <= m and ir <= r):
#             if comp1 <= comp2:
#                 temp = arr[k]
#                 z1 = ir
#                 if (arr[k] != comp1):
#                     arr[z1] = temp
#                 arr[k] = comp1
#                 il += 1
#                 k += 1
#                 if (il <= m):
#                     comp1 = arr[il]
#             else:
#                 temp = arr[k]
#                 arr[k] = comp2
#                 arr[ir] = temp
#                 k += 1
#                 ir += 1
#                 if (ir <= r):
#                     comp2 = arr[ir]

#     def mergeSort(self, arr, l, r):
#         if len(arr) == 1:
#             return 0
#         if (l < r):
#             m = int((l+r)/2)
#             print(m)
#             self.mergeSort(arr[l:m+1], l, m)
#             self.mergeSort(arr[m+1:r+1], m+1, r)
#             self.merge(arr, l, m, r)

# sol = Solution()
# a = [10, 5, 6, 9, 2]
# sol.mergeSort(a,0,4)
# # sol.merge(a,0,0,1)
# a


################# Solution ##########################

# This code is contributed by 29AjayKumar
# Python program in-place Merge Sort

# Merges two subarrays of arr.
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
# Inplace Implementation



class Solution:
    def merge(self, arr, start, mid, end):
        start2 = mid + 1

        # If the direct merge is already sorted
        if (arr[mid] <= arr[start2]):
            return

        # Two pointers to maintain start
        # of both arrays to merge
        while (start <= mid and start2 <= end):

            # If element 1 is in right place
            if (arr[start] <= arr[start2]):
                start += 1
            else:
                value = arr[start2]
                index = start2

                # Shift all the elements between element 1
                # element 2, right by 1.
                while (index != start):
                    arr[index] = arr[index - 1]
                    index -= 1

                arr[start] = value

                # Update all the pointers
                start += 1
                mid += 1
                start2 += 1


# '''
# * l is for left index and r is right index of
# the sub-array of arr to be sorted
# '''

    def mergeSort(self, arr, l, r):
        if (l < r):

            # Same as (l + r) / 2, but avoids overflow
            # for large l and r
            m = l + (r - l) // 2

            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)

            self.merge(arr, l, m, r)


    # ''' UTILITY FUNCTIONS '''
    # ''' Function to pran array '''


    def printArray(self, A, size):

        for i in range(size):
            print(A[i], end=" ")
        print()


    # # ''' Driver program to test above functions '''
    # if __name__ == '__main__':
    #     arr = [12, 11, 13, 5, 6, 7]
    #     arr_size = len(arr)

    #     self.mergeSort(arr, 0, arr_size - 1)
    #     self.printArray(arr, arr_size)


sol = Solution()
a = [10, 5, 6, 9, 2]
sol.mergeSort(a,0,4)
# sol.merge(a,0,0,1)
a