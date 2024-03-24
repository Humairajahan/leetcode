# 3090. Maximum Length Substring With Two Occurrences

# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.


# Example 1
# ---------
# Input: s = "bcbbbcba"
# Output: 4
# Explanation:
# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

# Example 2
# ---------
# Input: s = "aaaa"
# Output: 2
# Explanation:
# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".


# Brute force approach
# Time complexity O(n**3)
# Space complexity O(n)


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_length = 0
        s = list(s)
        for i in range(len(s) - 1):
            for j in range(i, len(s) - 1):
                sub_str = s[i : j + 2]
                count = 0
                z = {}
                for t in range(len(sub_str)):
                    if sub_str[t] in z:
                        z[sub_str[t]] += 1
                    else:
                        z[sub_str[t]] = 1
                    count = max(count, z[sub_str[t]])

                if count <= 2:
                    max_length = max(max_length, t + 1)
                else:
                    break

        return max_length
