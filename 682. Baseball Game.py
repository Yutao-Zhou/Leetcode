class Solution:
    def calPoints(self, ops: List[str]) -> int:
        i = 0
        ops.append(0)
        while 1:
            if i == len(ops) - 1:
                break
            try:
                ops[i] = int(ops[i])
                i += 1
            except:
                if ops[i] == "C":
                    del ops[i]
                    del ops[i - 1]
                    ops.append(0)
                    ops.append(0)
                    i -= 1
                if ops[i] == "D":
                    ops[i] = ops[i - 1] * 2
                    i += 1
                if ops[i] == "+":
                    ops[i] = ops[i - 2] + ops[i - 1]
                    i += 1
        return sum(ops)