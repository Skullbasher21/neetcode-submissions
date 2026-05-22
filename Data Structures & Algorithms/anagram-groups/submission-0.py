class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            existing = res.get(sortedS, [])
            existing.append(s)
            res[sortedS] = existing
        return list(res.values())