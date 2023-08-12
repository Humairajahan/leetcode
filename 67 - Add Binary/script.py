class Solution:
    def convertToBinary(self, a: str) -> int:
        a = a[::-1]
        result = 0
        for i in range(len(a)):
            result += int(a[i]) * pow(2, i)
        return result

    def addBinary(self, a: str, b: str) -> str:
        a = self.convertToBinary(a)
        b = self.convertToBinary(b)
        result = a + b
        return str(bin(result))[2:]


s = Solution()

test_case_1 = s.addBinary(a="11", b="1")
print(test_case_1)

test_case_2 = s.addBinary(a="1010", b="1011")
print(test_case_2)
