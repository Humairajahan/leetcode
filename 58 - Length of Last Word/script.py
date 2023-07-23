class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        while "" in words:
            words.remove("")
        return len(words[-1])


s = Solution()

test_case_1 = s.lengthOfLastWord(s="Hello World")
print(test_case_1)

test_case_2 = s.lengthOfLastWord(s="   fly me   to   the moon  ")
print(test_case_2)

test_case_3 = s.lengthOfLastWord(s="luffy is still joyboy")
print(test_case_3)
