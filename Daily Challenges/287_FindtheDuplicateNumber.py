# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.


# Example 1
# ---------
# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2
# ---------
# Input: nums = [3,1,3,4,2]
# Output: 3

# Example 3
# ---------
# Input: nums = [3,3,3,3,3]
# Output: 3


from typing import List


# HashMap
# Time complexity O(n)
# Space complexity O(n)


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        z = {}
        for i in nums:
            if i in z:
                return i
            else:
                z[i] = 1


print(Solution().findDuplicate(nums=[1, 3, 4, 2, 2]))

print(Solution().findDuplicate(nums=[3, 1, 3, 4, 2]))

print(Solution().findDuplicate(nums=[3, 3, 3, 3, 3]))
