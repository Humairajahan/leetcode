from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        q, r = divmod(len(nums), 3)
        majority_elements = []
        z = {}
        for i in range(len(nums)):
            if nums[i] not in z:
                z[nums[i]] = 1
            else:
                z[nums[i]] += 1
            if z[nums[i]] > q and nums[i] not in majority_elements:
                majority_elements.append(nums[i])
        return majority_elements


s = Solution()

test_case_1 = s.majorityElement(nums=[3, 2, 3])
print(test_case_1)

test_case_2 = s.majorityElement(nums=[1])
print(test_case_2)

test_case_3 = s.majorityElement(nums=[1, 2])
print(test_case_3)
