class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        #### simulation ####
        # i = 0
        # remain = list(range(n))
        # while len(remain) > 1:
        #     i = (i + k-1) % len(remain)
        #     remain.pop(i)
        # return remain[0] + 1
        
        #### que ####
        que = deque(range(n))
        counter = k
        while len(que) > 1:
            while counter :
                node = que.popleft()
                que.append(node)
                counter -= 1
            que.pop()
            counter = k
        return que[0] + 1