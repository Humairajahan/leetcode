class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if len(s) != len(t):
            return False
        for idx in range(len(t)):
            if s[idx] != t[idx]:
                return False
        return True


s = Solution()

test_case_1 = s.isAnagram(s="anagram", t="nagaram")
print(test_case_1)

test_case_2 = s.isAnagram(s="rat", t="car")
print(test_case_2)
