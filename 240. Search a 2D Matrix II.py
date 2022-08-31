class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #### BFS From Center ####
        # m, n = len(matrix), len(matrix[0])
        # queue = deque([(m // 2, n // 2)])
        # seen = set()
        # while queue:
        #     node = queue.popleft()
        #     if 0 <= node[0] < m and 0 <= node[1] < n:
        #         if matrix[node[0]][node[1]] == target:
        #             return True
        #         if node not in seen:
        #             seen.add(node)
        #             queue.append((node[0] - 1, node[1]))
        #             queue.append((node[0] + 1, node[1]))
        #             queue.append((node[0], node[1] - 1))
        #             queue.append((node[0], node[1] + 1))
        # return False
        
        #### BFS with early stop ####
        # m, n = len(matrix), len(matrix[0])
        # queue = deque([(0, 0)])
        # while queue:
        #     current = queue.popleft()
        #     if current[0] < m and current[1] < n:
        #         if matrix[current[0]][current[1]] == target:
        #             return True
        #         if matrix[current[0]][current[1]] < target:
        #             queue.append((current[0] + 1, current[1]))
        #             queue.append((current[0], current[1] + 1))
        # return False
        
        #### Start From bottom left ####
        # m, n = len(matrix), len(matrix[0])
        # i, j = m - 1, 0
        # while -1 < i and j < n:
        #     if matrix[i][j] == target:
        #         return True
        #     elif matrix[i][j] > target:
        #         i -= 1
        #     elif matrix[i][j] < target:
        #         j += 1
        # return False
        
        #### Binary search row by row ####
        l = len(matrix[0])
        for row in matrix:
            left, right = 0, l - 1
            if row[left] == target or row[right] == target:
                return True
            while left < right:
                mid = (left + right) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    left = mid + 1
                elif row[mid] > target:
                    right = mid
        return False