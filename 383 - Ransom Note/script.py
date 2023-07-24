class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for idx in range(len(ransomNote)):
            if ransomNote[idx] in magazine:
                magazine = magazine.replace(ransomNote[idx], "", 1)
            else:
                return False
        return True
    
    
s = Solution()

test_case_1 = s.canConstruct(ransomNote = "a", magazine = "b")
print(test_case_1)

test_case_2 = s.canConstruct(ransomNote = "aa", magazine = "ab")
print(test_case_2)

test_case_3 = s.canConstruct(ransomNote = "aa", magazine = "aab")
print(test_case_3)
