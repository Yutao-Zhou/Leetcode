class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #### BFS ####
        # color = image[sr][sc]
        # if color == newColor:
        #     return image
        # que = deque()
        # que.append((sr, sc))
        # while que:
        #     node = que.popleft()
        #     if 0 <= node[0] < len(image) and 0 <= node[1] < len(image[0]):
        #         if image[node[0]][node[1]] == color:
        #             image[node[0]][node[1]] = newColor
        #             que.append((node[0] - 1, node[1]))
        #             que.append((node[0], node[1] + 1))
        #             que.append((node[0] + 1, node[1]))
        #             que.append((node[0], node[1] - 1))
        # return image
    
        #### DFS ####
        color = image[sr][sc]
        if color == newColor:
            return image
        stack = []
        stack.append((sr, sc))
        while stack:
            node = stack.pop()
            if 0 <= node[0] < len(image) and 0 <= node[1] < len(image[0]):
                if image[node[0]][node[1]] == color:
                    image[node[0]][node[1]] = newColor
                    stack.append((node[0] - 1, node[1]))
                    stack.append((node[0], node[1] + 1))
                    stack.append((node[0] + 1, node[1]))
                    stack.append((node[0], node[1] - 1))
        return image