from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        lst = [*range(1, n + 1)]
        lst = list(map(str, lst))
        lst.sort()
        lst = list(map(int, lst))
        return lst


s = Solution()

test_case_1 = s.lexicalOrder(n=13)
print(test_case_1)

test_case_2 = s.lexicalOrder(n=2)
print(test_case_2)
