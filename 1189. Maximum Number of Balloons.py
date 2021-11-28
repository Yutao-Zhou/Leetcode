class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ##### countain #####
        # frequency = {"b":0,"a":0,"l":0,"o":0,"n":0}
        # for i in text:
        #     if i == "b":
        #         frequency["b"] += 1
        #     if i == "a":
        #         frequency["a"] += 1
        #     if i == "l":
        #         frequency["l"] += 1
        #     if i == "o":
        #         frequency["o"] += 1
        #     if i == "n":
        #         frequency["n"] += 1
        # possible = min(frequency["l"],frequency["o"]) // 2
        # if min(frequency["b"],frequency["a"],frequency["n"]) < possible:
        #     possible = min(frequency["b"],frequency["a"],frequency["n"])
        # return possible
        
        ##### better counter #####
        frequency = {"b":0,"a":0,"l":0,"o":0,"n":0}
        for i in text:
            if i == "b":
                frequency["b"] += 1
            if i == "a":
                frequency["a"] += 1
            if i == "l":
                frequency["l"] += 1
            if i == "o":
                frequency["o"] += 1
            if i == "n":
                frequency["n"] += 1
        return min(frequency["l"] // 2,frequency["o"] // 2,frequency["b"],frequency["a"],frequency["n"]) 