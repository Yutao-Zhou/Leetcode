class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        #### filter and check ####
        # def findOnce(s):
        #     ans = set()
        #     frequency = {}
        #     s = s.split(" ")
        #     for i in s:
        #         if i in frequency:
        #             frequency[i] += 1
        #         else:
        #             frequency[i] = 1
        #     for key in frequency.keys():
        #         if frequency[key] == 1:
        #             ans.add(key)
        #     return ans, s
        # S1, s1 = findOnce(s1)
        # S2, s2 = findOnce(s2)
        # ans = []
        # for i in S1:
        #     if i not in s2:
        #         ans.append(i)
        # for i in S2:
        #     if i not in s1:
        #         ans.append(i)
        # return ans
        
        #### frequency map ####
        ans = []
        freq = {}
        s1 = (s1 + " " + s2).split(" ")
        for w in s1:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1
        for key in freq.keys():
            if freq[key] == 1:
                ans.append(key)
        return ans