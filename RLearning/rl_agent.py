import random

class RLAgent():
  def __init__(self, color: str):
    self.name = f'RL-Agent-{color}'.capitalize()
    self.color = color
    self.symbol = color[0].capitalize()

  def add_to_game(self, game):
    self.game = game
    self.board = game.board

  def choose_action(self):
    return random.randint(0, len(self.game.grid[0]) - 1)

  def place_block(self):
    column = self.choose_action()
    column_valid = self.board.validate_move(column)
    return self.board.place_block(column, self.symbol)