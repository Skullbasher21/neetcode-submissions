class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(board)
        w = len(board[0])
        starts = []
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        for i in range(l):
            for j in range(w):
                if board[i][j] == word[0]:
                    s = set()
                    s.add((i,j))
                    starts.append(((i,j), word[1:len(word)], s))
        while starts:
            x,y,s = starts.pop()
            if y == "":
                return True
            for d1,d2 in dirs:
                z = (x[0]+ d1, x[1] + d2)
                if z not in s and z[0] >= 0 and z[1] >= 0 and z[0] < l and z[1] < w and board[z[0]][z[1]] == y[0]:
                    starts.append((z, y[1:len(word)], s | {z}))
        return False
            


        