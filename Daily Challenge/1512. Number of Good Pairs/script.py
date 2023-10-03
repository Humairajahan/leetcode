from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        pairs = 0
        for i in range(len(nums)):
            temp_nums = nums[i + 1 :]
            for j in range(len(temp_nums)):
                if nums[i] == temp_nums[j]:
                    pairs += 1
        return pairs


s = Solution()

test_case_1 = s.numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3])
print(test_case_1)

test_case_2 = s.numIdenticalPairs(nums=[1, 1, 1, 1])
print(test_case_2)

test_case_3 = s.numIdenticalPairs(nums=[1, 2, 3])
print(test_case_3)
