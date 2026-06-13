class Solution:
    def confusingNumber(self, n: int) -> bool:
        #1. Rotate n
        rotations = {0:0, 1:1, 6:9, 8:8, 9:6}
        num = n
        cur_num = 0
        while num>0:
            last_digit = num%10
            if last_digit not in rotations:
                return False
            cur_num = (cur_num*10) + rotations[last_digit]
            num //= 10
        return cur_num != n