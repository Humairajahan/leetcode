### Naive / Brute force Approach I : Converting to string


class Solution:
    def isPalindrome(self, x: int) -> bool:
        l2r = str(x)
        r2l = l2r[::-1]
        return l2r == r2l


### Naive / Brute force Approach II : Without converting to string


class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed_num = 0
        original_num = x
        if x < 0:
            return False
        while x > 0:
            q, r = divmod(x, 10)
            reversed_num = reversed_num * 10 + r
            x = q
        return reversed_num == original_num


s = Solution()

test_case1 = s.isPalindrome(x=121)
print(test_case1)

test_case2 = s.isPalindrome(x=-121)
print(test_case2)

test_case3 = s.isPalindrome(x=10)
print(test_case3)
