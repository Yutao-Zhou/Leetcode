class Solution:
    def judgeCircle(self, moves: str) -> bool:
        c = {"L":0, "R":0, "U":0, "D":0}
        for i in moves:
            c[i] += 1
        if c["L"] - c["R"] == 0 and c["U"] - c["D"] == 0:
            return True
        else:
            return False