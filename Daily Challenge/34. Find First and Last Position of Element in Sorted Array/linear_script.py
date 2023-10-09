from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        pos = []

        if len(nums) < 1:
            return [-1, -1]

        for i in range(len(nums)):
            if (nums[i] == target) and (len(pos) == 0):
                pos.append(i)
            elif (nums[i] == target) and (len(pos) == 1):
                pos.append(i)
            elif (nums[i] == target) and (len(pos) == 2):
                pos[-1] = i

        if len(pos) == 0:
            return [-1, -1]
        if len(pos) == 1:
            return [pos[0], pos[0]]

        return pos


s = Solution()

test_case_1 = s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8)
print(test_case_1)

test_case_2 = s.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6)
print(test_case_2)

test_case_3 = s.searchRange(nums=[], target=0)
print(test_case_3)

test_case_4 = s.searchRange(nums=[1], target=1)
print(test_case_4)
