class TrieNode:
    def __init__(self, char=None):
        self.char = char
        self.child = {}


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        #### Trie ####
        ans = 0
        root = TrieNode()
        for word in words:
            last = root
            for i in range(len(word) - 1, -1, -1):
                if word[i] not in last.child:
                    last.child[word[i]] = TrieNode(word[i])
                last = last.child[word[i]]
        stack = []
        for value in root.child.values():
            stack.append((value, 1))
        while stack:
            node, length = stack.pop()
            if node.child:
                for value in node.child.values():
                    stack.append((value, length + 1))
            else:
                ans += length + 1
        return ans