class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        total = 0
        l = 0
        m = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            m = max(m, count[s[r]])
            while (r - l + 1) - m > k:
                count[s[l]] -= 1
                l += 1
            total = max(total, r - l + 1)
        return total