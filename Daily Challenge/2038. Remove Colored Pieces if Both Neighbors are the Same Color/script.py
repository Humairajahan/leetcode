class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        sections = {"A": [], "B": []}
        word = ""
        for i in range(len(colors)):
            if len(word) != 0 and (word[-1] == colors[i]):
                word += colors[i]
            elif len(word) == 0:
                word += colors[i]
            else:
                if len(word) >= 3:
                    sections[word[0]].append(word)
                word = colors[i]
        if len(word) >= 3:
            sections[word[0]].append(word)

        alice = 0
        bob = 0
        for i in sections:
            for items in sections[i]:
                if i == "A":
                    alice += len(items) - 2
                if i == "B":
                    bob += len(items) - 2
        if alice > bob:
            return True
        else:
            return False


s = Solution()

test_case_1 = s.winnerOfGame(colors="AAABABB")
print(test_case_1)

test_case_2 = s.winnerOfGame(colors="AA")
print(test_case_2)

test_case_3 = s.winnerOfGame(colors="ABBBBBBBAAA")
print(test_case_3)
