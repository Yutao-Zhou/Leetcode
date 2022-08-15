class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #### Calculate and sort ####
        # for i in range(len(points)):
        #     points[i] = [points[i][0] ** 2 + points[i][1] ** 2] + points[i]
        # points.sort(key = lambda x: x[0])
        # points = points[:k]
        # for i in range(len(points)):
        #     points[i] = points[i][1:]
        # return points
        
        #### Minheap with heapq ####
        # import heapq
        # heap = []
        # for p in points:
        #     if len(heap) == k:
        #         heapq.heappushpop(heap, (-p[0] * p[0] - p[1] * p[1], p[0], p[1]))
        #     else:
        #         heapq.heappush(heap, (-p[0] * p[0] - p[1] * p[1], p[0], p[1]))
        # return [(x,y) for (dist,x, y) in heap]
        
        #### Minheap implement with list ####
        # heap = []
        # for p in points:
        #     if k > 0:
        #         heap.append([p[0] * p[0] + p[1] * p[1]] + p)
        #         heap.sort()
        #         k -= 1
        #     elif p[0] * p[0] + p[1] * p[1] < heap[-1][0]:
        #         heap.append([p[0] * p[0] + p[1] * p[1]] + p)
        #         heap.sort()
        #         heap.pop()
        # for i in range(len(heap)):
        #     heap[i] = heap[i][1:]
        # return heap
        
        #### kNN search using kd-tree ####
        from scipy import spatial
        tree = spatial.KDTree(points)
		# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)
        distance, idx = tree.query(x=[0,0], k=k, p=2) 
        return [points[i] for i in idx] if k > 1 else [points[idx]]