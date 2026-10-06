class Solution:
    def confusingNumber(self, n: int) -> bool:
        mappings = {0:0, 1:1, 6:9, 8:8, 9:6}
        num = 0
        x = n
        while n > 0:
            cur = n%10
            if cur not in mappings:
                return False
            num = (num*10) + mappings[cur]
            n //= 10
        return True if num != x else False