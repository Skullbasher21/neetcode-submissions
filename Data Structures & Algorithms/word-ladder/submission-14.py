class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        if endWord not in wordList:
            return 0
        q1 = deque([(beginWord, 1)])
        q2 = deque([(endWord, 1)])
        l = len(beginWord)
        seen1 = set()
        seen2 = set()
        seen1.add(beginWord)
        seen2.add(endWord)
        wset = set(wordList)
        while q1 and q2:
            if len(q1) > len(q2):
                q2, q1 = q1, q2
                seen1, seen2 = seen2, seen1
            x,y = q1.popleft()
            if x in seen2:
                return y + q2.pop()[1] - 1
            for i in range(l):
                for s in string.ascii_lowercase:
                    z = x[0:i] + s + x[i+1:]
                    if z in seen2:
                        return y + q2.pop()[1]
                    if z in wset and z not in seen1:
                        q1.append((z, y+1))
                        seen1.add(z)
            
        return 0
