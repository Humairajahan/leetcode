# 525. Contiguous Array

# Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.


# Example 1
# ---------
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

# Example 2
# ---------
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.


from typing import List


# HashMap
# Time complexity O(n)
# Space complexity O(n)


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        z = {}
        max_len = 0
        one_count, zero_count = 0, 0

        for i, num in enumerate(nums):
            if num == 1:
                one_count += 1
            else:
                zero_count += 1

            diff = one_count - zero_count
            if diff not in z:
                z[diff] = i

            if one_count == zero_count:
                max_len = one_count * 2
            else:
                max_len = max(max_len, (i - z[diff]))

        return max_len
