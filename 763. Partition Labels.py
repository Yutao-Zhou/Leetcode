class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #### Start and End Map ####
        # ans = []
        # segmentMap = [i for i in range(len(s))]
        # for i in range(len(s)):
        #     for j in range(i + 1, len(s)):
        #         if s[j] == s[i]:
        #             segmentMap[i] = max(segmentMap[i], j)
        # start, end = 0, segmentMap[0]
        # for i in range(len(segmentMap)):
        #     if i <= end:
        #         end = max(end, segmentMap[i])
        #     else:
        #         ans.append(end - start + 1)
        #         start = i
        #         end = segmentMap[start]
        # ans.append(end - start + 1)
        # return ans
        
        #### End index of each letter ####
        ans = []
        endIndex = [0] * 26
        for i in range(len(s)):
            endIndex[ord(s[i]) - 97] = i
        start = 0
        end = endIndex[ord(s[start]) - 97]
        for i in range(len(s)):
            if i <= end:
                end = max(end, endIndex[ord(s[i]) - 97])
            else:
                ans.append(end - start + 1)
                start = i
                end = endIndex[ord(s[start]) - 97]
        ans.append(end - start + 1)
        return ans