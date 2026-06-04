# Your goal is to implement a function, solve_sudoku(), that takes a two-dimensional 
# list of lists representing an unsolved Sudoku puzzle as the input argument and 
# returns a 9x9 two-dimensional list-of-lists containing the puzzle solution.

def solve_sudoku(puzzle):
  # find an empty cell
  for i in range(9):
    for j in range(9):
      if puzzle[i][j] == 0:
        # try all possible numbers
        for num in range(1, 10):
          if is_valid(puzzle, i, j, num):
            puzzle[i][j] = num
            if solve_sudoku(puzzle):
              return puzzle
            puzzle[i][j] = 0
  return puzzle

def is_valid(puzzle, i, j, num):
  # check row
  for k in range(9):
    if puzzle[i][k] == num:
      return False
  # check column
  for k in range(9):
    if puzzle[k][j] == num:
      return False
  # check 3x3 box
  box_x = i // 3
  box_y = j // 3
  for k in range(3):
    for l in range(3):
      if puzzle[box_x*3 + k][box_y*3 + l] == num:
        return False
  return True

test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print(solve_sudoku(test_puzzle)) 