class Solution:
    def frequencySort(self, s: str) -> str:
        #### frequency table ####
        # ans = ""
        # freq = {}
        # seen = set()
        # for c in s:
        #     if c in freq:
        #         freq[c] += 1
        #     if c not in freq:
        #         freq[c] = 1
        # while any(freq.values()):
        #     for char in freq.keys():
        #         if char not in seen:
        #             if freq[char] == max(freq.values()):
        #                 ans = ans + char * freq[char]
        #                 freq[char] = 0
        #                 seen.add(char)
        # return ans
        
        #### lambda sort dic ####
        # ck = {}
        # ans = []
        # for i in s:
        #     if i not in ck:
        #         ck[i] = 0
        #     if i in ck:
        #         ck[i] += 1
        # ck = sorted(ck.items(), key=lambda item: item[1])
        # for i in ck:
        #     ans.append(i[0]*i[1])
        # ans = "".join(ans)[::-1]
        # return ans