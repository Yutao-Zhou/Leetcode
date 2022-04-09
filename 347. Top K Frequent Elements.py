class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #### map ####
        # freq = {}
        # ans = []
        # seen = set()
        # for n in nums:
        #     if n in freq:
        #         freq[n] += 1
        #     if n not in freq:
        #         freq[n] = 1
        # while k > 0:
        #     for key in freq.keys():
        #         if key not in seen:
        #             if freq[key] == max(freq.values()) and k > 0:
        #                 ans.append(key)
        #                 freq[key] = 0
        #                 k -= 1
        #                 seen.add(key)
        # return ans
        
        #### for fun ####
        # return [k for k, v in Counter(nums).most_common(k)]
        
        #### heap ####
        if k == len(nums):
            return nums
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)