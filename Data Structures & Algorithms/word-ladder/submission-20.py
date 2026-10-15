class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        seen = {beginWord: 1}
        q = deque([beginWord])
        wset = set(wordList)
        while q:
            x = q.popleft()
            for i in range(len(x)):
                for j in string.ascii_lowercase:
                    x2 = x[:i] + j + x[i+1:]
                    if x2 in wset and x2 not in seen:
                        if x2 == endWord:
                            return seen[x] + 1
                        seen[x2] = seen[x] + 1
                        q.append(x2)
        return 0
                    
                
                