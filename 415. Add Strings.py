class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
#         n1 = 0
#         n2 = 0
#         for i in range(-1,-len(num1)-1,-1):
#             n1 += int(num1[i])*10**abs(i+1)
#         for i in range(-1,-len(num2)-1,-1):
#             n2 += int(num2[i])*10**abs(i+1)
#         return str(n1 + n2)
        
        n1 = []
        n2 = []
        for i in num1:
            n1.append(int(i))
        for i in num2:
            n2.append(int(i))
        if len(n1) > len(n2):
            for i in range (-1,-len(n2)-1,-1):
                n1[i] += n2[i]
            for i in range (-1,-len(n1)-1,-1):
                n1[i] = str(n1[i])
            return "".join(n1)
        if len(n1) < len(n2):
            for i in range (-1,-len(n1)-1,-1):
                n2[i] += n1[i]
            for i in range (-1,-len(n2)-1,-1):
                n2[i] = str(n2[i])
            return "".join(n2)
        