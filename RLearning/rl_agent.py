import random
from connect_four_game import BaseAgent
import numpy as np

class RLAgent(BaseAgent):
  def __init__(self, color: str, initial_exploration_rate=0.9):
    self.name = f'RL-Agent-{color.capitalize()}'
    self.color = color
    self.symbol = color[0].capitalize()
    self.initialize_weights()
    self.exploration_rate_percentage = initial_exploration_rate * 100
    self.exploration_decrease_rate = 0.01

  def initialize_weights(self):
    pass

  def choose_action(self):
    if random.randint(0, 100) < self.exploration_rate_percentage:
      return random.randint(0, len(self.game.grid[0]) - 1)
    else:
      return self.choose_best_action()

  def choose_best_action(self):
    # encode the board state as a vector and actions as a vector
    # multiply the vector by the weights
    # return the column with the highest value

    return random.randint(0, len(self.game.grid[0]) - 1)

  def place_block(self):
    column = self.choose_action()
    return self.board.place_block(column, self.symbol)

  def post_evaluation_hook(self):
    self.exploration_rate_percentage -= self.exploration_decrease_rate
    print(f'exploration rate: {self.exploration_rate_percentage}%')
    # check if game is over, if it is then update weights
    # save weights to file