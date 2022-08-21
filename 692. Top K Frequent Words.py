class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        #### two way dictionary ####
        ans = []
        w2f = {}
        f2w = {}
        for w in words:
            if w in w2f:
                w2f[w] += 1
            if w not in w2f:
                w2f[w] = 1
            if w2f[w] not in f2w:
                f2w[w2f[w]] = set([w])
            if w2f[w] in f2w:
                f2w[w2f[w]].add(w)
            if w2f[w] - 1 in f2w:
                f2w[w2f[w] - 1].remove(w)
        freq = sorted(list(f2w.keys()))
        while k > 0:
            ans.extend(sorted(f2w[freq[-1]])[:k])
            k -= len(sorted(f2w[freq[-1]])[:k])
            freq.pop()
        return ans