class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        #### set cache without thinking ####
        # ans = 0
        # vowel = set(["a", "e", "i", "o", "u"])
        # for i in range(len(word) - 3):
        #     for j in range(i + 4, len(word)):
        #         if set(list(word[i:j + 1])) == vowel:
        #             ans += 1
        # return ans
        
        #### two pointer and cache ####
        ans = 0
        vowel = set(["a", "e", "i", "o", "u"])
        for i in range(len(word)):
            if word[i] in vowel:
                cache = set(word[i])
                for j in range(i + 1, len(word)):
                    if word[j] in vowel:
                        cache.add(word[j])
                        if len(cache) == 5:
                            ans += 1
                    else:
                        break
        return ans