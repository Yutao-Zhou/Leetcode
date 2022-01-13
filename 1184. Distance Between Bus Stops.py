class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start <= destination:
            root1 = sum(distance[start:destination])
            root2 = sum(distance[destination:] + distance[:start])
        if start > destination:
            root1 = sum(distance[destination:start])
            root2 = sum(distance[start:] + distance[:destination])
        return min(root1,root2)