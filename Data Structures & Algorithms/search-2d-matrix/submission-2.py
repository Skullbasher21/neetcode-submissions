class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            if matrix[i][0] > target:
                for j in range(col):
                    if matrix[i-1][j] == target:
                        return True
                    if matrix[i-1][j] > target:
                        break
                break
            elif matrix[i][0] == target:
                return True
        for j in range(col):
            if matrix[-1][j] == target:
                return True
            if matrix[-1][j] > target:
                break
        return False