class Node:
    def __init__(self, val = None, children = None, isWord = False):
        self.val = val
        self.children = list()
        self.isWord = isWord
        
class WordDictionary:
#     def __init__(self):
#         self.root = Node()

#     def addWord(self, word: str) -> None:
#         dummy = self.root
#         for s in word:
#             isIn = False
#             for idx,n in enumerate(dummy.children):
#                 if n.val == s:
#                     dummy = dummy.children[idx]
#                     isIn = True
#                     break
#             if not isIn:
#                 dummy.children.append(Node(s))
#                 dummy = dummy.children[-1]
#         dummy.isWord = True

#     def search(self, word: str) -> bool:
#         #### BFS ####
#         wl, queue = len(word), deque([(self.root, 0)])
#         while queue:
#             n = queue.popleft()
#             if n[1] < wl:
#                 if word[n[1]] == ".":
#                     for c in n[0].children:
#                           queue.append((c, n[1] + 1))
#                 else:
#                     for c in n[0].children:
#                         if c.val == word[n[1]]:
#                             queue.append((c, n[1] + 1))
#                             break
#             elif n[1] == wl and n[0].isWord:
#                 return True
#         return False
        
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        dummy = self.root
        for s in word:
            isIn = False
            for idx,n in enumerate(dummy.children):
                if n.val == s:
                    dummy = dummy.children[idx]
                    isIn = True
                    break
            if not isIn:
                dummy.children.append(Node(s))
                dummy = dummy.children[-1]
        dummy.isWord = True

    def search(self, word: str) -> bool:
        #### DFS ####
        wl, stack = len(word), [(self.root, 0)]
        while stack:
            n = stack.pop()
            if n[1] < wl:
                if word[n[1]] == ".":
                    for c in n[0].children:
                          stack.append((c, n[1] + 1))
                else:
                    for c in n[0].children:
                        if c.val == word[n[1]]:
                            stack.append((c, n[1] + 1))
                            break
            elif n[1] == wl and n[0].isWord:
                return True
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)