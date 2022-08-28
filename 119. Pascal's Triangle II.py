class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #### Brute Force Recursive ####
        def buildN(lastRow, n):
            if n == rowIndex:
                nonlocal ans
                ans = lastRow
                return
            current = [1]
            for i in range(1, n + 1):
                current.append(lastRow[i] + lastRow[i - 1])
            current.append(1)
            buildN(current, n + 1)
        ans = None
        buildN([1], 0)
        return ans