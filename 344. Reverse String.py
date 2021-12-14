class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        ###### cache force swap ######
        # cach = ""
        # for i in range(len(s) // 2):
        #     cach = s[i]
        #     s[i] = s[-i-1]
        #     s[-i-1] = cach
        
        ##### swap easy ######
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]