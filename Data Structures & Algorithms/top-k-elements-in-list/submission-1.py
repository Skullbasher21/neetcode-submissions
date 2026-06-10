class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        c = Counter(nums)
        l = c.most_common(k)
        toReturn = []
        for i in l:
            toReturn.append(i[0])
        return toReturn