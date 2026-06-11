class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        i = 0
        j = 0
        current = ""
        while j <= len(s) - 1:
            if s[j] in current:
                ind = current.index(s[j])
                print(ind)
                current = current[ind + 1:len(current)]
                current += s[j]
                
                i = ind + 1
                j += 1
            else:
                current += s[j]
                j += 1
            print(current)
            m = max(m, len(current))
        return m
            


        