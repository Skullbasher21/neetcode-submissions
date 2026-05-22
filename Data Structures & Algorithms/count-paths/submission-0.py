import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = m + n
        return int(math.factorial(c - 2)/(math.factorial(m - 1) * math.factorial(n - 1)))
        