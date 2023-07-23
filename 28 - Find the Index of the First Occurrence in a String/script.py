class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            window_size = len(needle)
            no_of_slides = len(haystack) - len(needle) + 1
            for idx in range(no_of_slides):
                if needle == haystack[idx : idx + window_size]:
                    return idx
        else:
            return -1


s = Solution()

test_case_1 = s.strStr(haystack="sadbutsad", needle="sad")
print(test_case_1)

test_case_2 = s.strStr(haystack="leetcode", needle="leeto")
print(test_case_2)

test_case_3 = s.strStr(haystack="mississippi", needle="issip")
print(test_case_3)
