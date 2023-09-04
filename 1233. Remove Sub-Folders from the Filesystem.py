class TrieNode:
    def __init__(self, folder=None):
        self.folder = folder
        self.end = False
        self.sub_folder = {}


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        #### Trie ####
        root = TrieNode()
        for f in folder:
            last = root
            path = f.split("/")
            for p in path:
                if p not in last.sub_folder:
                    last.sub_folder[p] = TrieNode(p)
                last = last.sub_folder[p]
            last.end = True
        ans = []
        queue = deque()
        for value in root.sub_folder.values():
            queue.append((value, []))
        while queue:
            node, path = queue.popleft()
            if node.end:
                ans.append("/".join(path + [node.folder]))
            else:
                for value in node.sub_folder.values():
                    queue.append((value, path + [node.folder]))
        return ans