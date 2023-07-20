from typing import List
import time


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pos = 0
        right_pos = len(height) - 1
        while left_pos < right_pos:
            width = right_pos - left_pos
            area = width * min(height[left_pos], height[right_pos])
            max_area = max(max_area, area)
            if height[left_pos] < height[right_pos]:
                left_pos += 1
            else:
                right_pos -= 1
        return max_area


s = Solution()

test_case1 = s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7])
print(test_case1)

test_case2 = s.maxArea(height=[1, 1])
print(test_case2)
