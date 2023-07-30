class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        stack = []
        s_cp = s.replace("-", "")
        q, r = divmod(len(s_cp), k)
        if r != 0:
            stack.append(s_cp[:r+1])
            s.replace(s_cp[:r+1], "")
        for idx in range(q):
            stack.append(s_cp[idx*k:idx*k+k])
        return "-".join(stack).upper()
    
    
s = Solution()

test_case_1 = s.licenseKeyFormatting(s = "5F3Z-2e-9-w", k = 4)
print(test_case_1)

test_case_2 = s.licenseKeyFormatting(s = "2-5g-3-J", k = 2)
print(test_case_2)

test_case_3 = s.licenseKeyFormatting(s = "2-5g-3-J", k = 2)
print(test_case_3)
