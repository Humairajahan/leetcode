from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        value = [digits[i] * (10 ** (len(digits) - i - 1)) for i in range(len(digits))]
        value = sum(value) + 1
        arr = list(map(int, str(value)))
        return arr


s = Solution()

test_case1 = s.plusOne(digits=[1, 2, 3])
print(test_case1)

test_case2 = s.plusOne(digits=[4, 3, 2, 1])
print(test_case2)

test_case3 = s.plusOne(digits=[9])
print(test_case3)
