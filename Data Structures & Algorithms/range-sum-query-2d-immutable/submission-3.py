class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        self.prefixsum = [[0]*len(matrix[0]) for i in range(len(matrix))]

        
        for i in range(len(matrix)):
            self.prefixsum[i][0] = self.matrix[i][0]
            for j in range(1,len(matrix[0])):
                self.prefixsum[i][j] = self.prefixsum[i][j-1] + self.matrix[i][j] 

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum = 0 

        for i in range(row1,row2+1):
                if col1 > 0:
                    sum += self.prefixsum[i][col2] - self.prefixsum[i][col1-1]
                else:    
                    sum += self.prefixsum[i][col2]
        return sum

        


# Your NumMatrix object will be instantiated and called as such:
# matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(2, 1, 4, 3)