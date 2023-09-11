class Solution:
    def firstUniqChar(self, s: str) -> int:
        for index in range(len(s)):
            if s.count(s[index]) < 2:
                return index
        return -1


s = Solution()

test_case_1 = s.firstUniqChar(s="leetcode")
print(test_case_1)

test_case_2 = s.firstUniqChar(s="loveleetcode")
print(test_case_2)

test_case_3 = s.firstUniqChar(s="aabb")
print(test_case_3)
