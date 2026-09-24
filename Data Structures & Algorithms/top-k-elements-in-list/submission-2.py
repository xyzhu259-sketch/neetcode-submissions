class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for s in nums:
            res[s]+=1
        sortedRes = sorted(res.items(), key = lambda x: x[1])
        fin = []
        while len(fin) < k:
            fin.append(sortedRes.pop()[0])
        return fin

