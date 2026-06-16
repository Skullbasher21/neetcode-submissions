class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        dirs = [(1,0), (-1,0),(0,1),(0,-1)]
        islands = 0
        def bfs(grid: List[List[str]], r: int, c: int):
            grid[r][c] = '0'
            from collections import deque
            q = deque([(r,c)])
            print(q)
            while q:
                x = q.popleft()
                for d in dirs:
                    newx = x[0] + d[0]
                    newy = x[1] + d[1]
                    if newx >= row or newx < 0 or newy >= col or newy < 0 or grid[newx][newy] == '0':
                        continue
                    if grid[newx][newy] == "1":
                        q.append((newx, newy)) 
                        grid[newx][newy] = '0'              
        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1":
                    print(r,c)
                    islands += 1
                    bfs(grid, r, c)
        return islands

        