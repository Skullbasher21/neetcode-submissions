class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        aslist = list(s1)
        for i in range(0, len(s2) - len(s1)+1):
            copy = aslist.copy()
            word = s2[i:i+len(s1)]
            wl = list(word)
            for j in range(len(aslist)):
                if aslist[j] not in wl or aslist[j] not in word:
                    break
                if j == len(aslist) - 1 and aslist[j] in word:
                    print(word)
                    return True
                
                wl.remove(aslist[j])
        return False
                