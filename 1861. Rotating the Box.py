class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        ans = [["" for _ in range(m)] for _ in range(n)]
        for row_index in range(m):
            i, j = 0, 0
            while i < n and j < n:
                while i < n and box[row_index][i] != "#":
                    i += 1
                j = i + 1
                while j < n and box[row_index][j] == "#":
                    j += 1
                if j < n:
                    if box[row_index][j] == ".":
                        box[row_index][i] = "."
                        box[row_index][j] = "#"
                        i += 1
                        j += 1
                    elif box[row_index][j] == "*":
                        i = j + 1
                        j = i + 1
        for i in range(m):
            for j in range(n):
                ans[j][m - i - 1] = box[i][j]
        return ans