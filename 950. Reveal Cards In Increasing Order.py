class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        #### sort and recreate ####
        deck.sort(reverse = True)
        ans = deque([deck[0]])
        for i in range(1, len(deck)):
            ans.appendleft(ans.pop())
            ans.appendleft(deck[i])
        return ans