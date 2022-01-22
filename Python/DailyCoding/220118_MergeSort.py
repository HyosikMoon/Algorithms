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
        mr = m+1
        temp = arr[l]
        k = 0

        while(l <= m and mr <= r):
            if (temp <= arr[mr]):
                temp2 = arr[k]
                arr[k] = temp
                temp = temp2
                l += 1
                k += 1


    def mergeSort(self, arr, l, r):
        if (l < h):
            m = (l+h)/2
            mergeSort(self, arr, l, m)
            mergeSort(self, arr, m+1, h)
            merge(self, arr, l, m, h)
            