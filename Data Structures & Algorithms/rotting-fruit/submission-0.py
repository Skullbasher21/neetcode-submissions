class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        ones = 0
        time = 0
        row = len(grid)
        col = len(grid[0])
        q = deque()
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ones += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
        while q and ones > 0:
            l = len(q)
            for i in range(l):
                r, c = q.popleft()
                for d in dirs:
                    newr, newc = r + d[0], c + d[1]
                    if (newr in range(len(grid)) and newc in range(len(grid[0])) and grid[newr][newc] == 1):
                        grid[newr][newc] = 2
                        q.append((newr,newc))
                        ones -= 1
                    
            time += 1
        return time if ones == 0 else -1

        