class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #### Brute Force ####
        ans = []
        il, ir, ju, jd = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        stateNo = 0
        while il <= ir and ju <= jd:
            if stateNo % 4 == 0:
                i = il
                while i <= ir:
                    ans.append(matrix[ju][i])
                    i += 1
                ju += 1
            elif stateNo % 4 == 1:
                j = ju
                while j <= jd:
                    ans.append(matrix[j][ir])
                    j += 1
                ir -= 1
            elif stateNo % 4 == 2:
                i = ir
                while i >= il:
                    ans.append(matrix[jd][i])
                    i -= 1
                jd -= 1
            elif stateNo % 4 == 3:
                j = jd
                while j >= ju:
                    ans.append(matrix[j][il])
                    j -= 1
                il += 1
            stateNo += 1
        return ans