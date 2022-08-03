class RandomizedSet:

    def __init__(self):
        self.hashtable = {}
        self.number = []        

    def insert(self, val: int) -> bool:
        if val not in self.hashtable:
            self.hashtable[val] = len(self.number)
            self.number.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.hashtable:
            s = self.number[-1]
            self.number[-1], self.number[self.hashtable[val]] = self.number[self.hashtable[val]], self.number[-1]
            self.hashtable[s] = self.hashtable[val]
            self.hashtable.pop(val)
            self.number.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.number[random.randint(0, len(self.number) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()