class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix[0]) - 1
        if matrix[low][low] > target:
            return False
        while low < len(matrix) and high >= 0:
            if matrix[low][high] == target:
                return True
            else:
                if matrix[low][high] < target:
                    low += 1
                else:
                    high -= 1
        return False