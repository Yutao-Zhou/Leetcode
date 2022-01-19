class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        #### math ####
        ans = 0
        for i in tickets:
            if i < tickets[k]:
                ans += i
            if i >= tickets[k]:
                ans += tickets[k]
        if k < len(tickets) - 1:
            for i in range(k + 1, len(tickets)):
                if tickets[i] >= tickets[k]:
                    ans -= 1
        return ans