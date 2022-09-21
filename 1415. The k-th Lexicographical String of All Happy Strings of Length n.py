class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(path, skip):
            if k <= 0 or len(path) == n:
                self.k -= 1
                if self.k == 0:
                    self.ans = path
                return
            for i in range(3):
                if i != skip:
                    backtrack(path + option[i], i)
        self.k = k
        self.ans = ""
        option = ["a", "b", "c"]
        backtrack("", 3)
        return self.ans