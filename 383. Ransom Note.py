class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        #### hash table ####
        # available = {}
        # for i in magazine:
        #     if i in available:
        #         available[i] += 1
        #     if i not in available:
        #         available[i] = 1
        # for i in ransomNote:
        #     if i in available:
        #         available[i] -= 1
        #         if available[i] < 0:
        #             return False
        #     if i not in available:
        #         return False
        # return True
    
        #### sort & pointer ####
        i = 0
        j = 0
        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)
        while i < len(ransomNote) and j < len(magazine):
            if ransomNote[i] == magazine[j]:
                i += 1
                j += 1
            elif ransomNote[i] > magazine[j]:
                j += 1
            elif ransomNote[i] < magazine[j]:
                return False
        if i == len(ransomNote):
            return True
        else:
            return False