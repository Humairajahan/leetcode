### Naive / Brute force Approach : Converting to string


class Solution:
    def isPalindrome(self, x: int) -> bool:
        l2r = str(x)
        r2l = l2r[::-1]
        return l2r == r2l


s = Solution()

test_case1 = s.isPalindrome(x=121)
print(test_case1)

test_case2 = s.isPalindrome(x=-121)
print(test_case2)

test_case3 = s.isPalindrome(x=10)
print(test_case3)
