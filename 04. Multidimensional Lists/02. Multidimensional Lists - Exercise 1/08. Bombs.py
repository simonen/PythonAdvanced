size = int(input())
matrix = [[j for j in map(int, input().split())] for i in range(size)]

for k in input().split():
    row, col = list(map(int, k.split(",")))
    damage = matrix[row][col]
    if damage <= 0:
        continue

    matrix[row][col] = 0
    top_row = row - 1
    end_row = row + 1
    left_col = col - 1
    right_col = col + 1

    if row == 0:
        top_row = 0
    if row == size - 1:
        end_row = size - 1
    if col == 0:
        left_col = 0
    if col == size - 1:
        right_col = size - 1
    # The 3x3 submatrix with the bomb at the center
    for i in range(top_row, end_row + 1):
        for j in range(left_col, right_col + 1):
            if matrix[i][j] > 0:
                matrix[i][j] -= damage

active_cells = 0
cell_sum = 0
for i in range(size):
    for j in range(size):
        if matrix[i][j] > 0:
            active_cells += 1
            cell_sum += matrix[i][j]

print(f'Alive cells: {active_cells}')
print(f'Sum: {cell_sum}')
for i in matrix:
    print(*i)
