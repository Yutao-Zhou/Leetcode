class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #### recursive ####
        visited = [0]
        stack = [0]
        current = 0
        while stack:
            current = stack.pop()
            for key in rooms[current]:
                if key not in visited:
                    visited.append(key)
                    stack.append(key)
        return len(visited) == len(rooms)