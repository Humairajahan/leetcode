from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        z = {}
        for num in nums:
            if num in z:
                z[num] += 1
            else:
                z[num] = 1

        steps = 0
        for num in z:
            q3, r3 = divmod(z[num], 3)
            q2, r2 = divmod(z[num], 2)
            if (q3 > 0) and (r3 != 0):
                if r3 == 2:
                    steps += q3 + 1
                else:
                    step_3 = q3 - 1
                    temp_q2, temp_r2 = divmod((z[num] - (step_3 * 3)), 2)
                    steps += step_3 + temp_q2
                z[num] = 0
            elif r3 == 0:
                steps += q3
                z[num] = 0
            elif r2 == 0:
                steps += q2
                z[num] = 0
            if z[num] != 0:
                return -1
        return steps


s = Solution()

test_case_1 = s.minOperations(nums=[2, 3, 3, 2, 2, 4, 2, 3, 4])
print(test_case_1)

test_case_2 = s.minOperations(nums=[2, 1, 2, 2, 3, 3])
print(test_case_2)

test_case_3 = s.minOperations(
    nums=[14, 12, 14, 14, 12, 14, 14, 12, 12, 12, 12, 14, 14, 12, 14, 14, 14, 12, 12]
)
print(test_case_3)
