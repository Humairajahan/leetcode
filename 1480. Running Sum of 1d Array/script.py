from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            nums[i + 1] = nums[i] + nums[i + 1]
        return nums


s = Solution()

test_case_1 = s.runningSum(nums=[1, 2, 3, 4])
print(test_case_1)

test_case_2 = s.runningSum(nums=[1, 1, 1, 1, 1])
print(test_case_2)

test_case_3 = s.runningSum(nums=[3, 1, 2, 10, 1])
print(test_case_3)
