from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        tackle_neg = nums[0] * nums[1] * nums[-1]
        tackle_pos = nums[-1] * nums[-2] * nums[-3]
        return max(tackle_neg, tackle_pos)


s = Solution()

test_case_1 = s.maximumProduct(nums=[1, 2, 3])
print(test_case_1)

test_case_2 = s.maximumProduct(nums=[1, 2, 3, 4])
print(test_case_2)

test_case_3 = s.maximumProduct(nums=[-1, -2, -3])
print(test_case_3)
