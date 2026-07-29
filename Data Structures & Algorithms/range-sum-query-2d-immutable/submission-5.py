class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.prefixsum = [[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for i in range(1,len(matrix)+1):
            for j in range(1,len(matrix[0])+1):
                self.prefixsum[i][j] = (self.prefixsum[i-1][j] 
                                       + self.prefixsum[i][j-1] 
                                       + self.matrix[i-1][j-1]
                                       - self.prefixsum[i-1][j-1])


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
 
        return (self.prefixsum[row2+1][col2+1] 
                - self.prefixsum[row1][col2+1]
                - self.prefixsum[row2+1][col1]
                + self.prefixsum[row1][col1] 
        )
               
# Your NumMatrix object will be instantiated and called as such:
# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(2, 1, 4, 3)