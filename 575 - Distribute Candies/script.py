from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        unique_candies = set(candyType)
        return int(min(len(candyType) / 2, len(unique_candies)))


s = Solution()

test_case_1 = s.distributeCandies(candyType=[1, 1, 2, 2, 3, 3])
print(test_case_1)

test_case_2 = s.distributeCandies(candyType=[1, 1, 2, 3])
print(test_case_2)

test_case_3 = s.distributeCandies(candyType=[6, 6, 6, 6])
print(test_case_3)
