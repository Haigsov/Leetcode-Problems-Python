def searchMatrix(self, matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    row = 0
    col = len(matrix[row]) - 1

    while (row < len(matrix) and col >= 0):
        if matrix[row][col] < target:
            row += 1
        elif matrix[row][col] > target:
            col -= 1
        else:
            return True
    
    return False