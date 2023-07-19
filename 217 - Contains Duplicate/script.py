from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        outcome = {}
        for idx in range(len(nums)):
            if nums[idx] in outcome:
                return True
            outcome[nums[idx]] = 1
        return False
    

s = Solution()

test_case1 = s.containsDuplicate(nums = [1,2,3,1])
print(test_case1)

test_case2 = s.containsDuplicate(nums = [1,2,3,4])
print(test_case2)

test_case3 = s.containsDuplicate(nums = [1,1,1,3,3,4,3,2,4,2])
print(test_case3)