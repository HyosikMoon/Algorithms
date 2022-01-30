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

class Solution:
    def merge(self, arr, l, m, r):
        il = l
        k = 0
        ir = m+1
        comp1 = arr[l]
        comp2 = arr[m+1]
        while(il <= m and ir <= r):
            if comp1 <= comp2:
                temp = arr[k]
                arr[k] = comp1
                arr[r-ir] = temp
                il += 1
                k += 1
                comp1 = arr[r-il]
            else:
                temp = arr[k]
                arr[k] = comp2
                arr[ir] = temp
                k += 1
                ir += 1
                comp2 = arr[ir]

    def mergeSort(self, arr, l, r):
        if (l < r):
            m = (l+r)/2
            mergeSort(self, arr[l:m+1], l, m)
            mergeSort(self, arr[m:r+1], m+1, r)
            merge(self, arr, l, m, r)

sol = Solution()
a = [3,5,1,2,6]
sol.merge(a,0,2,4)
a
