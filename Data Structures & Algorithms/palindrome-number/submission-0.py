class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        word = []
        for let in x_str:
            word.append(let)
        
        L,R = 0, len(word)-1
        while L < R:
            if word[L] != word[R]:
                return False
            L,R = L+1,R-1
        return True