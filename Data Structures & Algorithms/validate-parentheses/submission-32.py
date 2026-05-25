class Solution:
    def isValid(self, s: str) -> bool:
        # (, ), {, }, [, ]
        # If it is an open bracket add it to a stack..
        # If it is the close bracket see that an open bracket is first up in the stack to be matched; if the stack is empty (so no corresponding bracket), return None. If its different return False. Return True if you get out of the loop

        stack = []
        mapping = {"}":"{", "]":"[", ")":"("}
        for let in s:
            if let == "(" or let == "{" or let == "[":
                stack.append(let)
            else:
                if not stack or mapping[let] != stack.pop():
                    return False
                    # if it is an invalid character then just brush through?
        return True if not stack else False