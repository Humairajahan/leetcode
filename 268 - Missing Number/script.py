from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current_sum = sum(nums)
        expected_nums = list(range(0, len(nums) + 1))
        expected_sum = sum(expected_nums)
        return expected_sum - current_sum


s = Solution()

test_case_1 = s.missingNumber(nums=[3, 0, 1])
print(test_case_1)

test_case_2 = s.missingNumber(nums=[0, 1])
print(test_case_2)

test_case_3 = s.missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1])
print(test_case_3)
