
class Board:
  grid_width = 7
  grid_height = 6

  def __init__(self):
    gridline = []
    for i in range(self.grid_width):
        gridline.append('-')
    grid = []
    for i in range(self.grid_height):
        grid.append(list(gridline))

    print(f'grid has {len(grid)} rows and {len(grid[0])} columns')
    self.grid = grid
  
  def print_board(self):
    for i in range(self.grid_height):
      print(self.grid[i])
    print([f'{i}' for i in range(self.grid_width)])

  def place_block(self, column, symbol):
    print(f'placing column {column} with symbol {symbol}')
    row = False
    row = self.find_next_free_row(column)
    self.grid[row][column] = symbol
    return {
      'row': row,
      'column': column,
    }
  
  def validate_move(self, column):
    if column < 0 or column > 6:
      return False
    row = self.find_next_free_row(column)
    if row < 0 or row > self.grid_height:
      return False
    return True
  
  def find_next_free_row(self, column):
    row = -1
    for i in reversed(range(self.grid_height)):
      if self.grid[i][column] == '-':
        print(f'found free row {i}')
        row = i
        break

    return row
  
  def get_row(self, row):
    return self.grid[row]

  def get_column(self, column):
    return [row[column] for row in self.grid]

  def get_cell(self, row, column):
    return self.grid[row][column]