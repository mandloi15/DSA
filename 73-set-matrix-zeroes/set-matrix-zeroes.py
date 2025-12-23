class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows , cols = len(matrix) , len(matrix[0])
        rowtrack = [0 for _ in range(0, rows)]
        coltrack = [0 for _ in range(0, cols)]
        
        for i in range(0 , rows):
            for j in range(0 , cols):
                if matrix[i][j] == 0:
                    rowtrack[i] = -1
                    coltrack[j] = -1

        for i in range(0 , rows):
            for j in range(0 , cols):
                if rowtrack[i] == -1 or coltrack[j] == -1:
                    matrix[i][j] = 0
                