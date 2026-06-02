class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ogs = set(nums)
        toReturn = 0
        for o in ogs:
            maxsofar = 1
            if o - 1 not in ogs:
                while o + maxsofar in ogs:
                    maxsofar += 1
                toReturn = max(toReturn, maxsofar)
        return toReturn
                    
        
        