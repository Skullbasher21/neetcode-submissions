class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        seen1, seen2 = {beginWord: 1}, {endWord: 1}
        q1, q2 = deque([beginWord]), deque([endWord])
        wset = set(wordList)
        if endWord not in wset:
            return 0
        if beginWord == endWord:
            return 1
        while q1 and q2:
            if len(q1) > len(q2):
                seen1,seen2 = seen2,seen1
                q1,q2 = q2,q1
            x = q1.popleft()
            for i in range(len(x)):
                for j in string.ascii_lowercase:
                    x2 = x[:i] + j + x[i+1:]
                    if x2 in seen2:
                        return seen1[x] + seen2[x2]
                    if x2 in wset and x2 not in seen1:
                        seen1[x2] = seen1[x] + 1
                        q1.append(x2)
        return 0
                    
                
                