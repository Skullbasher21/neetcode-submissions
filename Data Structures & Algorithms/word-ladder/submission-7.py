class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        import string
        from collections import deque
        words = set(wordList)
        if endWord not in words:
            return 0

        q = deque([(beginWord, 1)])
        while q:
            word, dist = q.popleft()
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    nxt = word[:i] + c + word[i + 1:]
                    if nxt in words:              # valid and unvisited
                        if nxt == endWord:
                            return dist + 1
                        words.remove(nxt)         # mark visited on enqueue
                        q.append((nxt, dist + 1))
        return 0
