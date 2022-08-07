class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #### quick select ####
        if not nums: return
        left, mid, right = [], [], []
        pivot = random.choice(nums)
        for x in nums:
            if x > pivot:
                left.append(x)
            elif x == pivot:
                mid.append(x)
            else:
                right.append(x)
        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k - len(left) - len(mid))
        else:
            return mid[0]