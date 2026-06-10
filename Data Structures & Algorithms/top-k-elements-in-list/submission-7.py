class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        import heapq
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        heap = []
        for i, j in d.items():
            heapq.heappush(heap,(j,i))
            if len(heap) > k:
                heapq.heappop(heap)
        toreturn = []
        for i in heap:
            toreturn.append(i[1])

        return toreturn

        
        
        