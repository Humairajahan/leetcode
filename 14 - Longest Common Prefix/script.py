from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        v = sorted(strs)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans


s = Solution()

test_case_1 = s.longestCommonPrefix(strs=["flower", "flow", "flight"])
print(test_case_1)

test_case_2 = s.longestCommonPrefix(strs=["dog", "racecar", "car"])
print(test_case_2)
