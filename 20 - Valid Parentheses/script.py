class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s: 
            if c in '([{': 
                stack.append(c) 
            else: 
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False 
                stack.pop()
        return not stack 
                 
    
    
s = Solution()

test_case_1 = s.isValid(s = "()")
print(test_case_1)

test_case_2 = s.isValid(s = "()[]{}")
print(test_case_2)

test_case_3 = s.isValid(s = "(]")
print(test_case_3)
