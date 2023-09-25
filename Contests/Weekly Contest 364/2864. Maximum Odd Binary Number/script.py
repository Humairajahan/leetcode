class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        one_count = s.count("1")
        zero_count = s.count("0")
        t = ""
        if one_count == 1:
            for i in range(zero_count):
                t += "0"
            t += "1"
        else:
            for i in range(one_count - 1):
                t += "1"
            for i in range(zero_count):
                t += "0"
            t += "1"
        return t


s = Solution()

test_case_1 = s.maximumOddBinaryNumber(s="010")
print(test_case_1)

test_case_2 = s.maximumOddBinaryNumber(s="0101")
print(test_case_2)
