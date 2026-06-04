# Your goal is to implement a function, solve_sudoku(), that takes a two-dimensional 
# list of lists representing an unsolved Sudoku puzzle as the input argument and 
# returns a 9x9 two-dimensional list-of-lists containing the puzzle solution.

# The following import brings in the 'product' function from the itertools module.
# 'product' allows you to generate the Cartesian product of input iterables.
# In the context of Sudoku, it is often used to efficiently iterate over all combinations of row and column indices,
# such as all cells in the 9x9 grid, by doing: for i, j in product(range(9), repeat=2):
from itertools import product

def solve_sudoku(puzzle):
  for (row, col) in product(range(0, 9), repeat=2):
    if puzzle[row][col] == 0: # find an empty cell
      for num in range(1, 10): # try all possible numbers
        allowed = True
        # check if the number is allowed in the row, column, and 3x3 box
        for i in range(0, 9):
          if num in (puzzle[i][col], puzzle[row][i]):
            allowed = False
            break # if the number is not allowed, break the loop
        if allowed:
          puzzle[row][col] = num
          if trial := solve_sudoku(puzzle):
            return trial
          puzzle[row][col] = 0
      return False
  return puzzle

def print_sudoku(puzzle):
  # replace zeros with dashes
  puzzle = [['*' if num == 0 else num for num in row] for row in puzzle]
  print()
  for row in range(0, 9):
    if row % 3 == 0 and row != 0:
      print('-' * 33) #draw horizontal line
    for col in range(0, 9):
      if col % 3 == 0 and col != 0:
        print('|', end='') #draw vertical line
      print(f' {puzzle[row][col]} ', end='')
    print()
  print()

test_puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
               [6, 0, 0, 1, 9, 5, 0, 0, 0],
               [0, 9, 8, 0, 0, 0, 0, 6, 0],
               [8, 0, 0, 0, 6, 0, 0, 0, 3],
               [4, 0, 0, 8, 0, 3, 0, 0, 1],
               [7, 0, 0, 0, 2, 0, 0, 0, 6],
               [0, 6, 0, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 4, 1, 9, 0, 0, 5],
               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

print_sudoku(test_puzzle)
solution = solve_sudoku(test_puzzle)
print_sudoku(solution)