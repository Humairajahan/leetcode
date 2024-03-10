# 349. Intersection of Two Arrays

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.


# Example 1:
# ---------
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# ---------
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.


from typing import List


# Two Pointer approach
# Time Complexity O(nlogn)
# Space Complexity O(min(len(nums1), len(nums2))) -> O(n)


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        arr1 = list(set(nums1))
        arr2 = list(set(nums2))
        arr1.sort()
        arr2.sort()

        first, second = 0, 0
        while first < len(arr1) and second < len(arr2):
            if arr1[first] < arr2[second]:
                first += 1
            elif arr1[first] > arr2[second]:
                second += 1
            else:
                arr.append(arr1[first])
                first += 1
                second += 1
        return arr
