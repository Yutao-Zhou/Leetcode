class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ##### cache force swap ####
        # cach = ""
        # for i in range(len(s) // 2):
        #     cach = s[i]
        #     s[i] = s[-i-1]
        #     s[-i-1] = cach
        
        #### swap cheat ####
        # for i in range(len(s) // 2):
        #     s[i], s[-i-1] = s[-i-1], s[i]
        
        #### recursive swap ####
        def recursion(s, i, j):
            if i > j:
                return s
            else:
                s[i], s[j] = s[j], s[i]
                return recursion(s, i + 1, j - 1)
        recursion(s, 0, len(s) - 1)