from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx in range(len(nums)):
          if nums[idx] >= target:
            return idx
        if nums[-1] < target:
          return len(nums)


s = Solution()

test_case1 = s.searchInsert(nums = [1,3,5,6], target = 5)
print(test_case1)

test_case2 = s.searchInsert(nums = [1,3,5,6], target = 2)
print(test_case2)

test_case3 = s.searchInsert(nums = [1,3,5,6], target = 7)
print(test_case3)