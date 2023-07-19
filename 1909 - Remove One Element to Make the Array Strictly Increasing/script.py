from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for idx in range(2, len(nums)):
            if nums[idx-2] >= nums[idx]:
                return False
            return True
        
s = Solution()

test_case1 = s.canBeIncreasing(nums = [1,2,10,5,7])
print(test_case1)

test_case2 = s.canBeIncreasing(nums = [2,3,1,2])
print(test_case2)

test_case3 = s.canBeIncreasing(nums = [1,1,1])
print(test_case3)
