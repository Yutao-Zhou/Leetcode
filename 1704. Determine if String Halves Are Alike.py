class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        #### stright forward one pass ####
        difference = 0
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        for i in s[:len(s) // 2]:
            if i in vowels:
                difference += 1
        for j in s[len(s) // 2:]:
            if j in vowels:
                difference -= 1
        return difference == 0