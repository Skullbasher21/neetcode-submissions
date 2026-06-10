class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import Counter
        from collections import defaultdict
        d = defaultdict(list)
        for s in strs:
            c = sorted(s)
            d[tuple(c)].append(s)
        print(d)
        return list(d.values())