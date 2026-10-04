class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        rows = len(words)

        for r in range(rows):
            for c in range(len(words[r])):
                if c >= rows or r >= len(words[c]):
                    return False
                
                if words[r][c] != words[c][r]:
                    return False

        return True
                

