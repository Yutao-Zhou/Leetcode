class Solution:
    def countPoints(self, rings: str) -> int:
        #### index set ####
        # r = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        # g = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        # b = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
        # for nums in range(len(rings)):
        #     if rings[nums] == 'R':
        #         r[rings[nums + 1]] += 1
        #     if rings[nums] == 'G':
        #         g[rings[nums + 1]] += 1
        #     if rings[nums] == 'B':
        #         b[rings[nums + 1]] += 1
        # rl = []
        # gl = []
        # bl = []
        # for freq in r.items():
        #     if freq[1] != 0:
        #         rl.append(int(freq[0]))
        # for freq in g.items():
        #     if freq[1] != 0:
        #         gl.append(int(freq[0]))
        # for freq in b.items():
        #     if freq[1] != 0:
        #         bl.append(int(freq[0]))
        # length = []
        # length.append(len(rl))
        # length.append(len(gl))
        # length.append(len(bl))
        # length = min(length)
        # rl = set(rl)
        # gl = set(gl)
        # bl = set(bl)
        # ansl = rl.intersection(gl)
        # ansl = ansl.intersection(bl)
        # return len(ansl)
        
        #### shortter manual index intersection ####
        # rl = []
        # gl = []
        # bl = []
        # for i in range(len(rings)):
        #     if rings[i] == 'R':
        #         if int(rings[i + 1]) in rl:
        #             pass
        #         else:
        #             rl.append(int(rings[i + 1]))
        #     if rings[i] == 'G':
        #         if int(rings[i + 1]) in gl:
        #             pass
        #         else:
        #             gl.append(int(rings[i + 1]))
        #     if rings[i] == 'B':
        #         if int(rings[i + 1]) in bl:
        #             pass
        #         else:
        #             bl.append(int(rings[i + 1]))
        # rl.sort()
        # gl.sort()
        # bl.sort()
        # i = 0
        # j = 0
        # k = 0 
        # ans = 0
        # while i < len(rl) and j < len(gl) and k < len(bl):
        #     if rl[i] < gl[j]:
        #         i += 1
        #         pass
        #     elif rl[i] > gl[j]:
        #         j += 1 
        #         pass
        #     elif rl[i] < bl[k]:
        #         i += 1
        #         pass
        #     elif rl[i] > bl[k]:
        #         k += 1
        #         pass
        #     else:
        #         if rl[i] == gl[j] == bl[k]:
        #             ans += 1
        #             i += 1
        #             j += 1
        #             k += 1
        # return ans
        
        #### position color set ####
        position = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        i = 1
        ans = 0
        while i < len(rings):
            if rings[i - 1] not in  position[rings[i]]:
                position[rings[i]].append(rings[i - 1])
            i += 2
        for i in position.values():
            if len(i) == 3:
                ans += 1
        return ans