class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        #### maping lazy with set ####
        transform = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        maped = []
        cache = ""
        for i in words:
            for j in i:
                cache += transform[ord(j) - 97]
            maped.append(cache)
            cache = ""
        return len(set(maped))