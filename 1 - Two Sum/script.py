from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outcome = {}
        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in outcome:
                return [outcome[complement], idx]
            outcome[nums[idx]] = idx


s = Solution()

test_case1 = s.twoSum(nums=[2, 7, 11, 15], target=9)
print(test_case1)

test_case2 = s.twoSum(nums = [3,2,4], target = 6)
print(test_case2)

test_case3 = s.twoSum(nums = [3,3], target = 6)
print(test_case3)
