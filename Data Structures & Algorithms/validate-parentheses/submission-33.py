class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}
        for let in s:
            if let in brackets:
                if stack and stack.pop() == brackets[let]:
                    continue
                else:
                    return False
            elif let == "(" or let == "{" or let == "[":
                stack.append(let)
        return not stack