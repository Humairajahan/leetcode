class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        reverse = []
        for word in words:
            reverse.append(word[::-1])
        return " ".join(reverse)


s = Solution()

test_case_1 = s.reverseWords(s="Let's take LeetCode contest")
print(test_case_1)

test_case_2 = s.reverseWords(s="God Ding")
print(test_case_2)
