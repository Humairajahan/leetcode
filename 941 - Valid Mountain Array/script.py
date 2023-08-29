from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3:
            return False
        i = 1
        while i < n and arr[i] > arr[i - 1]:
            i += 1
        if i == 1 or i == n:
            return False
        while i < n and arr[i] < arr[i - 1]:
            i += 1
        return i == n


s = Solution()

test_case_1 = s.validMountainArray(arr=[2, 1])
print(test_case_1)

test_case_2 = s.validMountainArray(arr=[3, 5, 5])
print(test_case_2)

test_case_3 = s.validMountainArray(arr=[0, 3, 2, 1])
print(test_case_3)
