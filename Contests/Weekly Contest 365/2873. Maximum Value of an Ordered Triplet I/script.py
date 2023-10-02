from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums) - 1):
            num_i = nums[i]
            nums_j_k = nums[i + 1 :]
            for j in range(len(nums_j_k)):
                num_j = nums_j_k[j]
                nums_k = nums_j_k[j + 1 :]
                for k in range(len(nums_k)):
                    num_k = nums_k[k]
                    if num_i > num_j:
                        value = (num_i - num_j) * num_k
                        if value > max_val:
                            max_val = value
        return max_val


s = Solution()

test_case_1 = s.maximumTripletValue(nums=[12, 6, 1, 2, 7])
print(test_case_1)

test_case_2 = s.maximumTripletValue(nums=[1, 10, 3, 4, 19])
print(test_case_2)

test_case_3 = s.maximumTripletValue(nums=[1, 2, 3])
print(test_case_3)
