class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        seen = {beginWord: 1}
        q = deque([beginWord])
        while q:
            x = q.popleft()
            for i in range(len(x)):
                for j in wordList:
                    x2 = x[:i] + "*" + x[i+1:]
                    j2 = j[:i] + "*" + j[i+1:]
                    if x2 == j2 and j not in seen:
                        if j == endWord:
                            return seen[x] + 1
                        seen[j] = seen[x] + 1
                        q.append(j)
        return 0
                    
                #for j in string.ascii_lowercase:
                