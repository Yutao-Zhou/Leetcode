#### Trie ####
class TrieNode:

    def __init__(self, char=None):
        self.char = char
        self.end = False
        self.child = {}


class MagicDictionary:

    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            last = self.root
            for char in word:
                if char not in last.child:
                    last.child[char] = TrieNode(char)
                last = last.child[char]
            last.end = True

    def search(self, searchWord: str) -> bool:
        stack = []
        for value in self.root.child.values():
            stack.append((value, 0, False))
        while stack:
            current, i, diff = stack.pop()
            if i < len(searchWord):
                if i == len(searchWord) - 1:
                    if current.end and ((current.char == searchWord[i] and diff) or (current.char != searchWord[i] and not diff)):
                        return True
                elif current.char == searchWord[i]:
                    for value in current.child.values():
                        stack.append((value, i + 1, diff))
                elif current.char != searchWord[i] and not diff:
                    for value in current.child.values():
                        stack.append((value, i + 1, True))
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)