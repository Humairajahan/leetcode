class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for i in range(len(s) - 1):
            if val[s[i]] < val[s[i + 1]]:
                number -= val[s[i]]
            else:
                number += val[s[i]]
        number += val[s[-1]]
        return number


s = Solution()

test_case_1 = s.romanToInt(s="III")
print(test_case_1)

test_case_2 = s.romanToInt(s="LVIII")
print(test_case_2)

test_case_3 = s.romanToInt(s="MCMXCIV")
print(test_case_3)
