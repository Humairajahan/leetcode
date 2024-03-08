# 3005. Count Elements With Maximum Frequency

# You are given an array nums consisting of positive integers.

# Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

# The frequency of an element is the number of occurrences of that element in the array.


# Example 1
# ---------
# Input: nums = [1,2,2,3,1,4]
# Output: 4
# Explanation: The elements 1 and 2 have a frequency of 2 which is the maximum frequency in the array.
# So the number of elements in the array with maximum frequency is 4.

# Example 2
# ---------
# Input: nums = [1,2,3,4,5]
# Output: 5
# Explanation: All elements of the array have a frequency of 1 which is the maximum.
# So the number of elements in the array with maximum frequency is 5.


from typing import List


# Two Pointer Approach
# Time Complexity O(nlogn)
# Space Complexity O(n)
    

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums.sort()
        slow, fast = 0, 1
        length = len(nums)
        
        if length == 1:
            return 1

        z = {}
        max_freq = 0
        curr = 1

        while fast < length:    
            if nums[slow] == nums[fast]:
                fast += 1
                curr += 1
            else:
                z[nums[slow]] = curr
                max_freq = max(max_freq, curr)
                curr = 1
                slow = fast
                fast += 1
        if nums[slow] not in z:
            z[nums[slow]] = curr
            max_freq = max(max_freq, curr)
        
        n = 0
        for i in z:
            if z[i] == max_freq:
                n += max_freq
        return n


# Greedy Approach: Hash Table
# Time Complexity O(n)
# Space Complexity O(n)


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        max_freq = 0
        z = {}
        for i in nums:
            if i in z:
                z[i] += 1
            else:
                z[i] = 1
            max_freq = max(max_freq, z[i])

        n = 0
        for i in z:
            if z[i] == max_freq:
                n += max_freq
        return n
