class Solution:
    def calPoints(self, operations: List[str]) -> int:
        prev_records = []
        curTotal = 0
        for i in operations:
            x = prev_records[-1] if prev_records else -1
            if i == "D":
                curTotal += x*2
                prev_records.append(x*2)
            elif i == "C":
                curTotal -= prev_records.pop()
            elif i == "+":
                y = prev_records[-1] + prev_records[-2]
                curTotal += y
                prev_records.append(y)
            else:
                curTotal += int(i)
                prev_records.append(int(i))
        return curTotal