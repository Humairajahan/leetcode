class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for idx in range(len(t)):
            if t[idx] in s:
                s = s.replace(t[idx], "", 1)
            else:
                return t[idx]
            
            
s = Solution()

test_case_1 = s.findTheDifference(s = "abcd", t = "abcde")
print(test_case_1)

test_case_2 = s.findTheDifference(s = "", t = "y")
print(test_case_2)
