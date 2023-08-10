from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx in range(len(nums)):
            if nums[idx] == 0:
                nums.append(0)
                nums.remove(nums[idx])
        return nums


s = Solution()

test_case_1 = s.moveZeroes(nums=[0, 1, 0, 3, 12])
print(test_case_1)

test_case_2 = s.moveZeroes(nums=[0])
print(test_case_2)

test_case_3 = s.moveZeroes(nums=[0, 0, 1])
print(test_case_3)
