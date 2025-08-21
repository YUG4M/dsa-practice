matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matrix)
total = 0

for i in range(n):
    total += matrix[i][i]  # Primary diagonal
    total += matrix[i][n - 1 - i]  # Secondary diagonal

if n % 2 == 1:
    total -= matrix[n // 2][n // 2]  # Remove double counted center

print("Diagonal sum:", total)
