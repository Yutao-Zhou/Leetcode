class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        #### Recursion ####
        def processString(i, count, path):
            if i == len(s) and count == 4:
                ans.append(".".join(path))
                return
            if i == len(s) or count == 4:
                return
            if s[i] == "0":
                processString(i + 1, count + 1, path + ["0"])
            else:
                for j in range(i + 1, min(i + 4, len(s) + 1)):
                    if int(s[i : j]) <= 255:
                        processString(j, count + 1, path + [s[i : j]])
        ans = []
        processString(0, 0, [])
        return ans