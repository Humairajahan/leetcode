from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for idx in range(1, len(nums)):
            if nums[idx - 1] != nums[idx]:
                nums[k] = nums[idx]
                k += 1
        return k


s = Solution()

test_case1 = s.removeDuplicates(nums=[1, 1, 2])
print(test_case1)

test_case2 = s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(test_case2)
