class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            d = {}
            for j in range(len(board[i])):
                if board[i][j] in d:
                    d[board[i][j]] += 1
                else: 
                    d[board[i][j]] = 1
            for k in d.keys():
                if d[k] > 1 and k != ".": 
                    print(d.items())
                    print(k)
                    return False
        for i in range(len(board)):
            d = {}
            for j in range(len(board[i])):
                if board[j][i] in d:
                    d[board[j][i]] += 1
                else: 
                    d[board[j][i]] = 1
            for k in d.keys():
                print(d.items())
                print(k)
                if d[k] > 1 and k != ".": 
                    return False
        for i in range(3):
            for j in range(3):
                d = {}
                x = i * 3
                y = j * 3
                for k in range(x, x+3):
                    for q in range(y, y+3):
                        if board[k][q] in d:
                            d[board[k][q]] += 1
                        else: 
                            d[board[k][q]] = 1
                for k in d.keys():
                    print(d.items())
                    print(k)
                    if d[k] > 1 and k != ".": 
                        return False
        return True
                    
        