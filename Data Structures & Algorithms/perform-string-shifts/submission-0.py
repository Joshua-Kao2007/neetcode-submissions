class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        str_list = []
        for let in s:
            str_list.append(let)

        for direction, amt in shift:
            amt = amt%len(s)
            if direction == 0: # left shift
                first_let = str_list[:amt] 
                str_list = str_list[amt:] + first_let
            if direction == 1: # right shift
                last_let = str_list[len(s)-amt:]
                str_list = last_let + str_list[:len(s)-amt]
        return "".join(str_list)
