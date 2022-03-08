class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        #### trust list ####
        # if trust == []:
        #     if n == 1:
        #         return 1
        #     else:
        #         return -1
        # people = []
        # for pair in trust:
        #     people.append(pair[1])
        # for pair in trust:   
        #     if pair[0] in people:
        #         people.remove(pair[0])
        # print(people)
        # for i in people:
        #     if people.count(i) == n - 1:
        #         return i
        # return -1
        
        #### graph out and in ####
        if trust == []:
            if n == 1:
                return 1
            else:
                return -1
        net = [0] * (n + 1)
        for pair in trust:
            net[pair[0]] -= 1
            net[pair[1]] += 1
        print(net)
        for i in range(len(net)):
            if net[i] == n - 1:
                return i
        return -1