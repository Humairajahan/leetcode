from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for c in range(len(accounts)):
            customer = accounts[c]
            wealth = 0
            for bank in range(len(customer)):
                wealth += customer[bank]
            if wealth > max_wealth:
                max_wealth = wealth
        return max_wealth


s = Solution()

test_case_1 = s.maximumWealth(accounts=[[1, 2, 3], [3, 2, 1]])
print(test_case_1)

test_case_2 = s.maximumWealth(accounts=[[1, 5], [7, 3], [3, 5]])
print(test_case_2)

test_case_3 = s.maximumWealth(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]])
print(test_case_3)
