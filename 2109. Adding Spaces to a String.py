class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        #### string slice, pancake (less space more time) ####
        # for i in range(-1,-len(spaces) - 1,-1):
        #     s = s[:spaces[i]] + " " + s[spaces[i]:]
        # return s
        
        #### append (more space less time) ####
        ans = []
        position = 0
        i = 0
        while position < len(s):
            if position == spaces[i]:
                ans.append(" ")
                if i < len(spaces) - 1:
                    i += 1
            ans.append(s[position])
            position += 1
        return "".join(ans)