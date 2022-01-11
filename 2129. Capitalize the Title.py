class Solution:
    def capitalizeTitle(self, title: str) -> str:
        #### string slicing ####
        # title = title.split(" ")
        # for i in range(len(title)):
        #     for j in range(len(title[i])):
        #         if len(title[i]) > 2 and j == 0:
        #             if ord("a") <= ord(title[i][j]) <= ord("z"):
        #                 title[i] = title[i][:j] + chr(ord(title[i][j]) - 32) + title[i][j + 1:]
        #         else:
        #             if ord("A") <= ord(title[i][j]) <= ord("Z"):
        #                 title[i] = title[i][:j] + chr(ord(title[i][j]) + 32) + title[i][j + 1:]
        # return " ".join(title)
        
        #### lower and capitalize ####
        ans = []
        title = title.split(" ")
        for s in title:
            if len(s) < 3:
                ans.append(s.lower())
            else:
                ans.append(s.capitalize())
        return " ".join(ans)