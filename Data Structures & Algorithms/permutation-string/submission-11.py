class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aslist = sorted(list(s1))
        for i in range(0, len(s2) - len(s1)+1):
            word = s2[i:i+len(s1)]
            wl = sorted(list(word))
            if wl == aslist:
                return True
        return False
                