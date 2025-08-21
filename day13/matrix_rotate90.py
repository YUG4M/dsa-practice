def rotate_matrix(matrix):
    transposed = [list(row) for row in zip(*matrix)]
    rotated = [row[::-1] for row in transposed]
    return rotated

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))
