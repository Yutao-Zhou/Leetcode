class Solution:
    def equalFrequency(self, word: str) -> bool:
        #### Brute Foce Hashmap ####
        counter = Counter(word)
        freq = Counter(counter.values())
        if len(freq) == 2:
            keys = list(freq.keys())
            if abs(keys[0] - keys[1]) == 1:
                if 1 in keys and freq[1] == 1: return True
                if keys[1] > keys[0]:
                    if freq[keys[1]] > 1:
                        return False
                elif keys[1] < keys[0]:
                    if freq[keys[0]] > 1:
                        return False
                return True
        elif len(freq) == 1:
            if 1 in freq: return True
            if len(counter) == 1: return True
        return False