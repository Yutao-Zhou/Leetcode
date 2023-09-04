class TrieNode():
    def __init__(self, char=None):
        self.isWord = False
        self.char = char
        self.child = {}

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        for word in words:
            last = root
            for c in word:
                if c in last.child:
                    last = last.child[c]
                else:
                    last.child[c] = TrieNode(c)
                    last = last.child[c]
            last.isWord = True
        queue = deque()
        ans = ""
        max_deepth = 0
        for value in root.child.values():
            queue.append((value, ""))
        while queue:
            current_level = []
            for i in range(len(queue)):
                node, word = queue.popleft()
                if node.isWord:
                    current_level.append(word + node.char)
                    for value in node.child.values():
                        queue.append((value, word + node.char))
            if current_level:
                current_level.sort()
                if len(ans) < len(current_level[0]):
                    ans = current_level[0]
                if len(ans) == len(current_level[0]):
                    ans = min(ans, current_level[0])
        return ans