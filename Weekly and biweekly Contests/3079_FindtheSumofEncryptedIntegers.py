# 3079. Find the Sum of Encrypted Integers

# You are given an integer array nums containing positive integers. We define a function encrypt such that encrypt(x) replaces every digit in x with the largest digit in x. For example, encrypt(523) = 555 and encrypt(213) = 333.

# Return the sum of encrypted elements.


# Example 1
# ---------
# Input: nums = [1,2,3]
# Output: 6
# Explanation: The encrypted elements are [1,2,3]. The sum of encrypted elements is 1 + 2 + 3 == 6.

# Example 2
# ---------
# Input: nums = [10,21,31]
# Output: 66
# Explanation: The encrypted elements are [11,22,33]. The sum of encrypted elements is 11 + 22 + 33 == 66.


from typing import List


# Greedy approach
# Time complexity O(n)
# Space complexity O(n)


class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        Sum = 0
        for num in nums:
            str_num = str(num)
            new_elem = max(str_num) * len(str_num)
            Sum += int(new_elem)
        return Sum
