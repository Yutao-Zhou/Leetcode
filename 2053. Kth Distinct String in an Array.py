class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ####  detect duplicate by list ####
        # distinct = []
        # cache = []
        # for character in arr:
        #     if character in distinct:
        #         cache.append(character)
        #         distinct.remove(character)
        #     if character not in distinct and character not in cache:
        #         distinct.append(character)
        # try:
        #     return distinct[k - 1]
        # except:
        #     return ""
        
        #### frequency dictionary ####
        frequency = {}
        for i in arr:
            if i in frequency:
                frequency[i] += 1
            if i not in frequency:
                frequency[i] = 1
        for i in frequency.items():
            if i[1] == 1:
                if k == 1:
                    return i[0]
                k -= 1
        return ""