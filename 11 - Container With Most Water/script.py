from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = []
        n = len(height)
        for idx in range(1, n):
            for jdx in range(n - idx):
                left_height = height[idx - 1]
                right_height = height[idx:][jdx]
                sub_area = (jdx + 1) * min(left_height, right_height)
                area.append(sub_area)
        return max(area)


s = Solution()

test_case1 = s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
print(test_case1)

test_case2 = s.maxArea(height=[1, 1])
print(test_case2)
