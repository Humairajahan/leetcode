class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s))
        s = s.lower()
        if s != s[::-1]:
            return False
        return True
    
    
s = Solution()

test_case_1 = s.isPalindrome(s = "A man, a plan, a canal: Panama")
print(test_case_1)

test_case_2 = s.isPalindrome(s = "race a car")
print(test_case_2)

test_case_3 = s.isPalindrome(s = " ")
print(test_case_3)
