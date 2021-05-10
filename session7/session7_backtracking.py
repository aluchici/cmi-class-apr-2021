# 9 x 9 sudoku, 3 x 3
import pprint 

# find next empty cell
def find_empty_cell(arr, l):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                l[0] = row
                l[1] = col
                return True
    return False

# check if value used in row 
def used_in_row(arr, row, value):
    for i in range(9):
        if arr[row][i] == value:
            return True
    return False

# check if value used in col 
def used_in_col(arr, col, value):
    for i in range(9):
        if arr[i][col] == value:
            return True
    return False

# check if value in 3 x 3 sub matrix
def used_in_box(arr, row, col, value):
    for i in range(3):
        for j in range(3):
            if arr[row + i][col + j] == value:
                return True
    return False

# check if value is valid at given location
def is_safe_location(arr, row, col, value):
    return not used_in_row(arr, row, value) and not used_in_col(arr, col, value) and not used_in_box(arr, row - row % 3, col - col % 3, value)

def solve(arr):
    l = [0, 0]
    if not find_empty_cell(arr, l):
        return True

    row = l[0]
    col = l[1]

    for digit in range(1, 10):
        if is_safe_location(arr, row, col, digit):
            arr[row][col] = digit

            if solve(arr):
                return True

            arr[row][col] = 0

    return False

if __name__ == "__main__":
    g = [[0 for x in range(9)] for y in range(9)]

    g = [[5, 0, 6, 0, 0, 8, 4, 0, 0],
          [3, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    pprint.pprint(g)
    if (solve(g)):
        pprint.pprint(g)
    else:
        print("No sol")
