class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        #### map both ####
        # ans = []
        # def process(string):
        #     mp = {}
        #     m = []
        #     counter = 0
        #     for c in string:
        #         if c in mp:
        #             m.append(mp[c])
        #         if c not in mp:
        #             mp[c] = counter
        #             m.append(counter)
        #             counter += 1
        #     return m
        # target = process(pattern)
        # for w in words:
        #     if target == process(w):
        #         ans.append(w)
        # return ans
        
        #### map onece ####
        ans = []
        def process(string):
            mp = {}
            m = ""
            seen = set()
            for i in range(len(string)):
                if string[i] in mp:
                    m += mp[string[i]]
                if string[i] not in mp:
                    if pattern[i] in seen:
                        return m
                    mp[string[i]] = pattern[i]
                    m += mp[string[i]]
                    seen.add(pattern[i])
            return m
        target = process(pattern)
        for w in words:
            if pattern == process(w):
                ans.append(w)
        return ans