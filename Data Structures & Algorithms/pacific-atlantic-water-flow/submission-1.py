class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row = len(heights)
        col = len(heights[0])
        toReturn = []
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        def dfs(heights: List[List[int]], i:int, j:int):
            stack = []
            stack.append((i,j))
            pacific = False
            atlantic = False
            visited = []
            while stack:
                x = stack.pop()
                visited.append(x)
                if x[0] == 0 or x[1] == 0:
                    pacific = True
                if x[0] == row - 1 or x[1] == col - 1:
                    atlantic = True
                if pacific and atlantic:
                    toReturn.append([i,j])
                    break
                for d in dirs:
                    newx = x[0] + d[0]
                    newy = x[1] + d[1]
                    if newx >= 0 and newy >= 0 and newx < row and newy < col and heights[x[0]][x[1]] >= heights[newx][newy] and (newx,newy) not in visited:
                        stack.append((newx,newy))

        for i in range(row):
            for j in range(col):
                dfs(heights, i, j)
        return toReturn
        