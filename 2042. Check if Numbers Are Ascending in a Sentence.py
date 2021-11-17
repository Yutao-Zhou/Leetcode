class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(" ")
        cach = 0
        for i in range(len(s)):
            try:
                s[i] = int(s[i])
                if s[i] <= cach:
                    return False
                else:
                    cach = s[i]
            except:
                pass
        return True