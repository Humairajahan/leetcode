from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = []
        range_of_nums = list(range(1, k + 1))
        for i in range(len(nums)):
            target = nums[-1]
            if (target in range_of_nums) and (target not in collection):
                collection.append(target)
            del nums[-1]
            if len(collection) == k:
                return i + 1
        return i + 1


s = Solution()

test_case_1 = s.minOperations(nums=[3, 1, 5, 4, 2], k=2)
print(test_case_1)

test_case_2 = s.minOperations(nums=[3, 1, 5, 4, 2], k=5)
print(test_case_2)

test_case_3 = s.minOperations(nums=[3, 2, 5, 3, 1], k=3)
print(test_case_3)
