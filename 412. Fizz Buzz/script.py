from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = []
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            else:
                if i % 3 == 0:
                    answer.append("Fizz")
                else:
                    if i % 5 == 0:
                        answer.append("Buzz")
                    else:
                        answer.append(str(i))
        return answer


s = Solution()

test_case_1 = s.fizzBuzz(n=3)
print(test_case_1)

test_case_2 = s.fizzBuzz(n=5)
print(test_case_2)

test_case_3 = s.fizzBuzz(n=15)
print(test_case_3)
