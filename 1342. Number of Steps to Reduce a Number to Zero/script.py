class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num != 0:
            steps += 1
            if num % 2 == 0:
                num = num / 2
            else:
                num -= 1
        return steps


s = Solution()

test_case_1 = s.numberOfSteps(num=14)
print(test_case_1)

test_case_2 = s.numberOfSteps(num=8)
print(test_case_2)

test_case_3 = s.numberOfSteps(num=123)
print(test_case_3)
