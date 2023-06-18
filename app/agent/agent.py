from app.board.board import Board

class Agent():
  def __init__(self, name: str, color: str, board: Board):
    self.validate(color)
    self.name = name
    self.color = color
    self.symbol = color[0].capitalize()
    self.board = board
    print(f'{self.name} has entered the game as team {self.color}')
  
  def validate(self, color):
    valid_colors = ['red', 'blue']
    if color not in valid_colors:
      raise Exception(f'Invalid color {color}, use one of {valid_colors}')

  def place_block(self):
    column_valid = False
    while not column_valid:
      column = int(input("Choose a column (0-6): "))
      column_valid = self.board.validate_move(column)
      if column_valid:
        return self.board.place_block(column, self.symbol)
      else:
        print('Invalid column, try again')