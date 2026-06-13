class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        if not words:return True

        # while i loop. while j loop
        for col in range(len(words[0])):
            cur_col = []
            for row in range(len(words)):
                if len(words[row]) <= col:
                    break
                cur_col.append(words[row][col])
            if "".join(cur_col) != words[col]:
                return False
        return True

