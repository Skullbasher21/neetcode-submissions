class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        bestsofar = 0
        l = []
        for i in range(len(s)):
            if s[i] not in l:
                l.append(s[i])
            else: 
                
                l = l[l.index(s[i]) + 1:len(l)]
                l.append(s[i])
            bestsofar = max(bestsofar, len(l)) 
            

        return bestsofar

        