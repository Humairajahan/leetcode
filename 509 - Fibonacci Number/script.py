class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)
        
        
s = Solution()

test_case1 = s.fib(n=2)
print(test_case1)

test_case2 = s.fib(n=3)
print(test_case2)

test_case3 = s.fib(n=4)
print(test_case3)

test_case4 = s.fib(n=30)
print(test_case4)
        