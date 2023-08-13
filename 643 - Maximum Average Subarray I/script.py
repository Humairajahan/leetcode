from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = sum(nums[:k])
        for idx in range(len(nums) - k):
            current_sum = sum(nums[idx + 1 : idx + k + 1])
            max_sum = max(max_sum, current_sum)
        return max_sum / k


s = Solution()

test_case_1 = s.findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4)
print(test_case_1)

test_case_2 = s.findMaxAverage(nums=[5], k=1)
print(test_case_2)