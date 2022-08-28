class Solution:
    def myAtoi(self, s: str) -> int:
        ans, digits, negative = 0, [], False
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            elif s[i] == "+":
                i += 1
            elif s[i] == "-":
                negative = True
                i += 1
            break
        for j in range(i, len(s)):
            if "0" <= s[j] <= "9":
                digits.append(s[j])
                continue
            break
        l = len(digits)
        for i in range(l - 1, -1, -1):
            ans += int(digits[i]) * 10 ** (l - 1 - i)
        if negative:
            ans = -ans
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if ans < -2 ** 31:
            return -2 ** 31
        return ans