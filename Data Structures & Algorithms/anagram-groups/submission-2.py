class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            x = "".join(sorted(s))
            d[x].append(s)
        return list(d.values())
        