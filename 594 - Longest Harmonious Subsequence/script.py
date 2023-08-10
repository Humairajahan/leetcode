from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        z = 0
        unique_values = list(set(nums))
        unique_values.sort()
        for idx in range(len(unique_values) - 1):
            if unique_values[idx + 1] - unique_values[idx] == 1:
                subsequence_len = nums.count(unique_values[idx]) + nums.count(
                    unique_values[idx + 1]
                )
                z = max(z, subsequence_len)
        return z


s = Solution()

test_case_1 = s.findLHS(nums=[1, 3, 2, 2, 5, 2, 3, 7])
print(test_case_1)

test_case_2 = s.findLHS(nums=[1, 2, 3, 4])
print(test_case_2)

test_case_3 = s.findLHS(nums=[1, 1, 1, 1])
print(test_case_3)
