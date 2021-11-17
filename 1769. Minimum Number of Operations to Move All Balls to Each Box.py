class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # boxes = list(boxes)
        # ans = []
        # index = []
        # cache = 0
        # for i in range(len(boxes)):
        #     if boxes[i] == '1':
        #         index.append(i)
        # for i in range(len(boxes)):
        #     for j in index:
        #         cache += abs(j - i)
        #     ans.append(cache)
        #     cache = 0
        # return ans
        ans = [0]*len(boxes)
        leftCount = 0
        leftCost = 0
        rightCount = 0
        rightCost = 0
        for i in range (1,len(boxes)):
            if boxes[i-1] == "1":
                leftCount += 1
            leftCost += leftCount
            ans[i] = leftCost
        for i in range(len(boxes)-2,-1,-1):
            if boxes[i+1] == "1":
                rightCount += 1
            rightCost += rightCount
            ans[i] += rightCost
        return ans