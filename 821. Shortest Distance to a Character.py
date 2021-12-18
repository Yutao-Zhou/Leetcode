class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        #### save index and go from there ####
        # index = []
        # ans = []
        # j = 1
        # for i in range(len(s)):
        #     if s[i] == c:
        #         index.append(i)
        # index.insert(0,index[0])
        # if len(index) == 1:
        #     for i in range(len(s)):
        #         ans.append(abs(i - index[0]))
        # else:
        #     for i in range(len(s)):
        #         if i > index[j] and j < len(index) - 1:
        #                 j += 1
        #         if i <= index[j] and j <= len(index) -1:
        #                 ans.append(min(abs(index[j] - i),abs(index[j - 1] - i)))
        #         elif j == len(index) - 1:
        #             ans.append(abs(i - index[j]))
        # return ans
    
        #### two pass: left and right ####
        index = -10000
        ans = [0]*len(s)
        for i in range(len(s)):
            if s[i] == c:
                index = i
            else:
                ans[i] = abs(i - index)
        index = -10000
        for i in range(-1,-len(s) - 1,-1):
            if s[i] == c:
                index = i
            else:
                ans[i] = min(ans[i],abs(i - index))
        return ans