class CombinationIterator:
    #### BackTrack and store all path ####
    def __init__(self, characters: str, combinationLength: int):
        def backTrack(path, remain):
            if len(path) == combinationLength:
                self.allPath.append(path)
                return
            for i in range(len(remain)):
                backTrack(path + remain[i], remain[i + 1:])
        self.allPath = deque()
        backTrack("", characters)
        
    def next(self) -> str:
        return self.allPath.popleft()

    def hasNext(self) -> bool:
        return self.allPath

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()