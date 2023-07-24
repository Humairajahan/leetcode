class Solution:
    def isHappy(self, n: int) -> bool:
        idx = 0
        n = list(str(n))
        while n != ["1"]:
            n = map(lambda x: int(x) ** 2, n)
            n = sum(n)
            n = list(str(n))
            idx += 1
            if idx > 20:
                return False
        return True


s = Solution()

test_case_1 = s.isHappy(n=19)
print(test_case_1)

test_case_2 = s.isHappy(n=2)
print(test_case_2)

test_case_3 = s.isHappy(n=7)
print(test_case_3)
