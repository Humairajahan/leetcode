class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def getEndResult(s: str):
            z = []
            for i in s:
                if i == "#" and z:
                    z.pop()
                elif i != "#":
                    z.append(i)
            return "".join(z)

        return getEndResult(s) == getEndResult(t)


s = Solution()

test_case_1 = s.backspaceCompare(s="ab#c", t="ad#c")
print(test_case_1)

test_case_2 = s.backspaceCompare(s="ab##", t="c#d#")
print(test_case_2)

test_case_3 = s.backspaceCompare(s="a#c", t="b")
print(test_case_3)
