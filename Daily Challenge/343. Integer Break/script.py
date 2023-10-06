class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1
        else:
            q, r = divmod(n, 3)
            if r == 0:
                return 3**q
            elif r == 1:
                return (3 ** (q - 1)) * 4
            elif r == 2:
                return (3**q) * 2


s = Solution()

test_case_1 = s.integerBreak(n=7)
print(test_case_1)

test_case_2 = s.integerBreak(n=8)
print(test_case_2)

test_case_3 = s.integerBreak(n=9)
print(test_case_3)
