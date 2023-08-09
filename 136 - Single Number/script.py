from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        z = {}
        for idx in nums:
            if idx in z:
                z[idx] += 1
            else:
                z[idx] = 1
        z = dict([(value, key) for key, value in z.items()])
        return z[1]


s = Solution()

test_case_1 = s.singleNumber(nums=[2, 2, 1])
print(test_case_1)

test_case_2 = s.singleNumber(nums=[4, 1, 2, 1, 2])
print(test_case_2)

test_case_3 = s.singleNumber(nums=[1])
print(test_case_3)
