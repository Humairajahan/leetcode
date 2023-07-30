import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ""
        while columnNumber > 0:
            columnNumber, r = divmod(columnNumber - 1, 26)
            s += string.ascii_uppercase[r]
        return s[::-1]
    
s = Solution()

test_case_1 = s.convertToTitle(columnNumber=1)
print(test_case_1)

test_case_2 = s.convertToTitle(columnNumber=28)
print(test_case_2)

test_case_3 = s.convertToTitle(columnNumber=701)
print(test_case_3)

test_case_4 = s.convertToTitle(columnNumber=2147483647)
print(test_case_4)
