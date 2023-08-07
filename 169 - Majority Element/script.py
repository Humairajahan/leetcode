from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for idx in range(len(nums)):
            if nums[idx] not in d:
                d[nums[idx]] = 0
            d[nums[idx]] += 1

        for jdx in d:
            if d[jdx] > len(nums) / 2:
                return jdx


s = Solution()

test_case_1 = s.majorityElement(nums=[3, 2, 3])
print(test_case_1)

test_case_2 = s.majorityElement(nums=[2, 2, 1, 1, 1, 2, 2])
print(test_case_2)
