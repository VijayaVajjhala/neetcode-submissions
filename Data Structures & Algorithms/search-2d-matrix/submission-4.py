class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        right = 0
        left = len(matrix[0]) - 1
        
        while right < len(matrix):
            if matrix[right][left] >= target:
                break
            elif matrix[right][left] < target:
                right += 1

        if right == len(matrix):
            return False



        idx = right
        right = 0
        left = len(matrix[0]) - 1
        while right <= left:
            mid = (right + left) // 2
            if matrix[idx][mid] > target:
                left = mid - 1
            elif matrix[idx][mid] < target:
                right = mid + 1
            else:
                return True
        return False

            

        