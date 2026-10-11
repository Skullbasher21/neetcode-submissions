class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        l = len(grid)
        w = len(grid[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        twos = []
        seen = set()
        m = 0
        for i in range(l):
            for j in range(w):
                if grid[i][j] == 2:
                    twos.append(((i,j), 0))
                    seen.add((i,j))
        from collections import deque
        q = deque(twos)
        while q:
            x = q.popleft()
            for d1,d2 in dirs:
                y = (x[0][0] + d1, x[0][1] + d2)
                if y not in seen and y[0] >= 0 and y[1] >= 0 and y[0] < l and y[1] < w and grid[y[0]][y[1]] == 1:
                    seen.add(y)
                    grid[y[0]][y[1]] = 2
                    q.append((y, x[1] + 1))
                    m = max(m, x[1] + 1)
        for i in range(l):
            for j in range(w):
                if grid[i][j] == 1:
                    return -1
        return m



        