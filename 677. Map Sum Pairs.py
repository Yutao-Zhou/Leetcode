class TrieNode:

    def __init__(self, char=None):
        self.char = char
        self.score = None
        self.child = {}


class MapSum:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, key: str, val: int) -> None:
        last = self.root
        for char in key:
            if char not in last.child:
                last.child[char] = TrieNode(char)
            last = last.child[char]
        last.score = val

    def sum(self, prefix: str) -> int:
        ans = 0
        last = self.root
        for char in prefix:
            if char not in last.child:
                return 0
            last = last.child[char]
        if last.score:
            ans += last.score
        stack = list(last.child.values())
        while stack:
            node = stack.pop()
            if node.score:
                ans += node.score
            stack.extend(list(node.child.values()))
        return ans
        

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)