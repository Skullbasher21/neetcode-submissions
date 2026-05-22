class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros = zeros + [(i,j)]
        for i,j in zeros:
            self.setzeros(matrix, i, j)
    
    def setzeros(self, matrix: List[List[int]], i: int, j: int) -> None:
        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                if a == i or b == j:
                    matrix[a][b] = 0
        