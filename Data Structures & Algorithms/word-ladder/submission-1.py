class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        import string
        l = len(beginWord)
        wordList.append(beginWord)
        wset = set(wordList)
        q = deque([(beginWord, 1)])
        from collections import defaultdict
        adj = defaultdict(list)
        for w in wordList:
            for i in range(l):
                for j in string.ascii_lowercase:
                    w2 = w[0:i] + j + w[i + 1:]
                    if w2 in wset and w2 != w:
                        adj[w].append(w2)
        seen = set(beginWord)
        while q:
            x,y = q.popleft()
            for s in adj[x]:
                if s == endWord:
                    return y + 1
                if s in seen:
                    continue
                seen.add(s)
                q.append((s, y + 1))
        return 0
