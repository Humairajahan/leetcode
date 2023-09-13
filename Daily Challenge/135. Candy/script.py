from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        z = {}
        for i in range(len(ratings) - 1):
            if ratings[i] not in z:
                z[ratings[i]] = 1
            if ratings[i + 1] not in z:
                z[ratings[i + 1]] = 1
            local_max = max(ratings[i], ratings[i + 1])
            z[local_max] += 1
        min_candy = 0
        for j in z:
            min_candy += z[j]
        return min_candy


s = Solution()

test_case_1 = s.candy(ratings=[1, 0, 2])
print(test_case_1)

test_case_2 = s.candy(ratings=[1, 2, 2])
print(test_case_2)

test_case_3 = s.candy(ratings=[1, 2, 87, 87, 87, 2, 1])
print(test_case_3)
