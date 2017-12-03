"""
You are given an m x n 2D image matrix (List of Lists) 
where each integer represents a pixel. 
Flip it in-place along its horizontal axis.

Example:

Input image :  
              1 1
              0 0 
Modified to :   
              0 0
              1 1
"""
def flip_horizontal_axis(matrix):
    # # [[1, 1], [0, 0]]
    # tempRow = matrix[0]
    # matrix[0] = matrix[1]
    # matrix[1] = tempRow
    
    if len(matrix[0]) < 2:
        return
    
    for iRow in range(len(matrix) / 2):
        tempRow = matrix[iRow]
        matrix[iRow] = matrix[len(matrix) - 1 - iRow]
        matrix[len(matrix) - 1 - iRow] = tempRow