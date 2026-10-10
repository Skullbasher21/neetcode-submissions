class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        count = 0
        dirs = [(1,0), (-1,0),(0,1),(0,-1)]
        def dfs(i,j,s):
            stack = [(i,j)]
            while stack:
                x = stack.pop()
                seen.add(x)
                for d in dirs:
                    y = (x[0] + d[0], x[1] + d[1])
                    if y not in seen and y[0] >= 0 and y[0] < len(grid) and y[1] >= 0 and y[1] < len(grid[0]) and grid[y[0]][y[1]] == "1":
                        stack.append(y)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) in seen:
                    continue
                if grid[i][j] == "1":
                    count += 1
                    dfs(i,j,seen)
                else:
                    seen.add((i,j))
        return count
        