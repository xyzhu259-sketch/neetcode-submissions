class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            Nword =  ''.join(sorted(s))
            res[Nword].append(s)
        return list(res.values())
