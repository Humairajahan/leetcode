class Solution:
    def firstUniqChar(self, s: str) -> int:
        for idx in range(len(s)):
            if s.count(s[idx]) < 2:
                return idx
        return -1

    
s = Solution()

test_case_1 = s.firstUniqChar(s = "leetcode")
print(test_case_1)

test_case_2 = s.firstUniqChar(s = "loveleetcode")
print(test_case_2)

test_case_3 = s.firstUniqChar(s = "aabb")
print(test_case_3)

test_case_4 = s.firstUniqChar(s = "aadadaad")
print(test_case_4)
