from typing import List
import time


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        s = set(nums)
        return [i for i in range(1, len(nums)+1) if i not in s]
    

s = Solution()

test_case_1 = s.findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1])
print(test_case_1)

test_case_2 = s.findDisappearedNumbers(nums = [1,1])
print(test_case_2)
