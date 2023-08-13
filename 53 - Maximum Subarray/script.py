from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]

        for num in nums[1:]:
            currentSum = max(num, currentSum + num)
            maxSum = max(maxSum, currentSum)

        return maxSum


s = Solution()

test_case_1 = s.maxSubArray(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(test_case_1)

test_case_2 = s.maxSubArray(nums=[1])
print(test_case_2)

test_case_3 = s.maxSubArray(nums=[5, 4, -1, 7, 8])
print(test_case_3)
