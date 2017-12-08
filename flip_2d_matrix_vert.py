def flip_vertical_axis(matrix):
    """
    my version
    """
    # [[1, 0], [1, 0]]
    if len(matrix[0]) < 2:
        return
    for row in matrix:
        for elem in range(len(row) // 2):
            temp = row[elem]
            row[elem] = row[len(row) - elem - 1]
            row[len(row) - elem - 1] = temp

matrix = [[1, 0], [1, 0]]
flip_vertical_axis(matrix)

for i in matrix:
    print(i)

def flip_2_vertical_axis(matrix):  
    """
    according to firecode.io
    """  
    r = len(matrix) - 1
    c = len(matrix[0]) - 1
    temp = 0
    i = 0
    while i <= r:
        j = 0
        while j <= (c/2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][c - j]
            matrix[i][c - j] = temp
            j = j + 1
        i = i + 1