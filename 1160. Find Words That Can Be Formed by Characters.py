class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #### cache dic, map and match ####
        ans = 0
        counter = 0
        cache = {}
        charsMap = {}
        for i in chars:
            if i in charsMap:
                charsMap[i] += 1
            if i not in charsMap:
                charsMap[i] = 1
        for word in words:
            counter = 0
            cache = {}
            for char in word:
                if char in cache:
                    cache[char] += 1
                if char not in cache:
                    cache[char] = 1
            for j in cache.items():
                if j[0] not in charsMap or j[1] > charsMap[j[0]]:
                    break
                counter += 1
            if counter == len(set(word)):
                ans += len(word)
        return ans