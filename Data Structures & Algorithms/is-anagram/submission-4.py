class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = list(s)
        t1 = list(t)
        for i in s1:
            if i in t1:
                t1.remove(i)
            else:
                return False
        if t1 != []:
            return False
        return True
        