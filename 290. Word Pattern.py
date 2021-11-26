class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ram = s.split(" ")
        ck = {}
        j = 0
        k = 0
        kk = {}
        pattern = list(pattern)
        for i in range(len(ram)):
            if ram[i] not in ck:
                ck[ram[i]] = chr(97 + j)
                j += 1
            if ram[i] in ck:
                ram[i] = ck[ram[i]]
        for i in range(len(pattern)):
            if pattern[i] not in kk:
                kk[pattern[i]] = chr(97 + k)
                k += 1
            if pattern[i] in kk:
                pattern[i] = kk[pattern[i]]
        if "".join(ram) == "".join(pattern):
            return True
        else:
            return False