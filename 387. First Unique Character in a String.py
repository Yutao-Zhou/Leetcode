class Solution:
    def firstUniqChar(self, s: str) -> int:
        #### que ####
        # seen = set()
        # i = 0
        # que = deque(list(s))
        # while que:
        #     char = que.popleft()
        #     if char not in que and char not in seen:
        #         return i
        #     else:
        #         i += 1
        #         seen.add(char)
        # return -1
        
        #### frequency table ####
        freq = [0] * 26
        for i in s:
            freq[ord(i) - 97] += 1
        for i in range(len(s)):
            if freq[ord(s[i]) - 97] == 1:
                return i
        return -1