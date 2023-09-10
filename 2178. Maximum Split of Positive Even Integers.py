class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        #### Backtrack ####
        def split(n, path, start):
            if n == 0:
                nonlocal ans
                if len(path) > len(ans):
                    ans = list(path)
                    return True
                return False
            
            for i in range(start, n + 1, 2):
                if i not in path:
                    path.add(i)
                    if split(n - i, path, i + 2):
                        return True
                    path.remove(i)

        ans = []
        if finalSum % 2:
            return ans
        split(finalSum, set(), 2)
        return ans