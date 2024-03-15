# 930. Binary Subarrays With Sum

# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

# A subarray is a contiguous part of the array.


# Example 1:
# ---------
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# Example 2
# ---------
# Input: nums = [0,0,0,0,0], goal = 0
# Output: 15


from typing import List


# Brute force Approach
# Time complexity O(n**2)
# Space complexity O(n)


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        num_of_sub_arr = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                sub_arr = nums[i : j + 1]
                if sub_arr.count(1) == goal:
                    num_of_sub_arr += 1
        return num_of_sub_arr
