class Solution:
    def romanToInt(self, s: str) -> int:
        #### iteritive ####
<<<<<<< HEAD
#         table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         ans = table[s[0]]
#         for i in range(1, len(s)):
#             ans += table[s[i]]
#             if table[s[i]] > table[s[i - 1]]:
#                 ans -= 2 * table[s[i - 1]]
#         return ans
        
        #### recursive ####
        table = {'I':1, 'V':5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        def recursive(table, s):
            if len(s) == 0:
                return 0 ## stopping recursion
            if len(s) >= 2 and s[:2] in table:
                return table[s[:2]] + recursive(table, s[2:])
            else:
                return table[s[0]] + recursive(table, s[1:])
        return recursive(table, s)
=======
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = table[s[0]]
        for i in range(1, len(s)):
            ans += table[s[i]]
            if table[s[i]] > table[s[i - 1]]:
                ans -= 2 * table[s[i - 1]]
        return ans
>>>>>>> 21931e36b5cd1d6da774ae678467814496de5cf6
