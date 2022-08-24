class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = dict()
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, word: str) -> None:
        dummy = self.root
        for s in word:
            if s not in dummy.children:
                dummy.children[s] = Node(s)
            dummy = dummy.children[s]
        dummy.children[True] = None

    def search(self, word: str) -> bool:
        dummy = self.root
        for s in word:
            if s in dummy.children:
                dummy = dummy.children[s]
            else:
                return False
        return True in dummy.children

    def startsWith(self, prefix: str) -> bool:
        dummy = self.root
        for s in prefix:
            if s in dummy.children:
                dummy = dummy.children[s]
            else:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)