from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for idx in range(len(nums)):
            if nums[idx] != val:
                nums[k] = nums[idx]
                k += 1
        return k
    
    
s = Solution()

test_case1 = s.removeElement(nums = [3,2,2,3], val = 3)
print(test_case1)

test_case2 = s.removeElement(nums = [0,1,2,2,3,0,4,2], val = 2)
print(test_case2)