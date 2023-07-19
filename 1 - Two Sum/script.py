from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outcome = {}
        for num in range(len(nums)):
            complement = target - nums[num]
            if nums[num] not in outcome:
                outcome[complement] = nums[num]
            return [nums[num], complement]
    

s = Solution().twoSum(nums = [2,7,11,15], target = 9)
print(s)