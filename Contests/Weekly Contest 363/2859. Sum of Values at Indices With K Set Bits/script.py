from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in range(len(nums)):
            bin_indice = str(bin(i))
            if bin_indice.count("1") == k:
                sum += nums[i]
        return sum


s = Solution()

test_case_1 = s.sumIndicesWithKSetBits(nums=[5, 10, 1, 5, 2], k=1)
print(test_case_1)

test_case_2 = s.sumIndicesWithKSetBits(nums=[4, 3, 2, 1], k=2)
print(test_case_2)
