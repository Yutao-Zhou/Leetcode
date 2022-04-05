class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        #### map ####
        # ans = []
        # strength = []
        # for row in mat:
        #     counter = 0
        #     for i in range(len(row)):
        #         if row[i] == 1:
        #             counter += 1
        #         if row[i] == 0 or i == len(row) - 1:
        #             strength.append(counter)
        #             counter = 0
        #             break
        # target = deque()
        # target.extend(sorted(strength))
        # p = 0
        # while p < len(target):
        #     hit = target[p]
        #     for i in range(len(strength)):
        #         if strength[i] == hit and i not in ans:
        #             ans.append(i)
        #             k -= 1
        #             p += 1
        #             if k == 0:
        #                 return ans
        #             break
        
        #### slow megic ####
        i = 0
        ans = []
        while i < len(mat[0]):
            for j in range(len(mat)):
                if mat[j][i] == 0 and j not in ans:
                    ans.append(j)
                    k -= 1
                    if k == 0:
                        return ans
            i += 1
        while k != 0:
            for i in range(len(mat)):
                if mat[i][0] == 1 and i not in ans:
                    ans.append(i)
                    k -= 1
        return ans