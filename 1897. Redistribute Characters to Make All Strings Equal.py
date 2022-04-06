class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        #### map check even or odd ####
        count = {}
        for word in words:
            for char in word:
                if char in count:
                    count[char] += 1
                if char not in count:
                    count[char] = 1
        for f in count.values():
            if f % len(words)  != 0:
                return False
        return True