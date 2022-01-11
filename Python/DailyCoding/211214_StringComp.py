# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of consecutive repeating characters in chars:

# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

# After you are done modifying the input array, return the new length of the array.

# You must write an algorithm that uses only constant extra space.
 

# Example 1:

# Input: chars = ["a","a","b","b","c","c","c"]
# Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
# Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
# Example 2:

# Input: chars = ["a"]
# Output: Return 1, and the first character of the input array should be: ["a"]
# Explanation: The only group is "a", which remains uncompressed since it's a single character.


class Solution:
    def compress(self, chars):
        # s = []

        # # Initial condition1 - for single element
        # if len(chars) == 1:
        #     return len(chars)

        # # Initial condition2
        # s.append(chars[0])
        # s.append(0)

        # # Compare the next element with the previous element
        # # Find them whether or not they are same
        # for c in chars:
        #     if s[-2] == c:
        #         s[-1] += 1
        #     else:
        #         if s[-1] == 1:
        #             s[-1] = c
        #             s.append(1)
        #         else:
        #             s[-1] = str(s[-1])
        #             s.append(c)
        #             s.append(1)

        # if s[-1] == 1:
        #     s.pop()
        # else:
        #     s[-1] = str(s[-1])
           
        # for i, e in enumerate(s):
        #     chars[i] = s[i]
        # chars.pop() 

        # return chars


        left = i = 0
        while i < len(chars):
            char, length = chars[i], 1

            # Count the number of same letters
            while (i + 1) < len(chars) and char == chars[i + 1]:
                length, i = length + 1, i + 1
            chars[left] = char

            # Update the number of same chars 
            # Update the indices for the next iteration
            if length > 1:
                len_str = str(length)
                chars[left + 1:left + 1 + len(len_str)] = len_str
                left += len(len_str)
            left, i = left + 1, i + 1
        return left

sol = Solution()
sol.compress(["a","a","b","b","b","b"])




# Input
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# Output
# ["a","b","12","b","b","b","b","b","b","b","b","b"]
# Expected
# ["a","b","1","2"]






## Optimal Solution
#         left = i = 0
#         while i < len(chars):
#             char, length = chars[i], 1
#             while (i + 1) < len(chars) and char == chars[i + 1]:
#                 length, i = length + 1, i + 1
#             chars[left] = char
#             if length > 1:
#                 len_str = str(length)
#                 chars[left + 1:left + 1 + len(len_str)] = len_str
#                 left += len(len_str)
#             left, i = left + 1, i + 1
#         return left