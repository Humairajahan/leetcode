from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def factorial(n):
            val = 1
            for i in range(1, n + 1):
                val *= i
            return val

        p = []
        for i in range(rowIndex + 1):
            val = factorial(rowIndex) / (factorial(i) * factorial(rowIndex - i))
            p.append(int(val))
        return p


s = Solution()

test_case_1 = s.getRow(rowIndex=3)
print(test_case_1)

test_case_2 = s.getRow(rowIndex=0)
print(test_case_2)

test_case_3 = s.getRow(rowIndex=1)
print(test_case_3)
