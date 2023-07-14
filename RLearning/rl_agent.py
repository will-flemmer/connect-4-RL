import random
from connect_four_game import BaseAgent
import numpy as np
from collections import deque
from .create_net import create_net

"""
Each square on the board will be represented by a number
Encoding:
  0: empty
  1: this agent
  2: other agent
"""

class RLAgent(BaseAgent):
  def __init__(self, color: str, initial_exploration_rate=1.0):
    self.name = f'RL-Agent-{color.capitalize()}'
    self.color = color
    self.symbol = color[0].capitalize()
    self.exploration_rate_percentage = initial_exploration_rate * 100
    self.exploration_decrease_rate = 0.01
    self.replay_memory = deque(maxlen=50_000)
    self.reward = 0

  def initialize_models(self):
    state_shape = (self.board.row_count * self.board.column_count,)
    action_shape = self.board.column_count
    self.model = create_net(state_shape, action_shape)
    self.target_model = create_net(state_shape, action_shape)
    self.target_model.set_weights(self.model.get_weights())
    self.steps_to_update_target_model = 0

  def initialize_state(self):
    self.prev_state = self.board.encode_board(self)
    self.current_state = self.board.encode_board(self)

  def post_add_to_game(self):
    self.initialize_models()
    self.initialize_state()

  def choose_action(self):
    if random.randint(0, 100) < self.exploration_rate_percentage:
      action = random.randint(0, len(self.game.grid[0]) - 1)
    else:
      action = self.choose_best_action()
    self.action = action
    return action

  def choose_best_action(self):
    return random.randint(0, len(self.game.grid[0]) - 1)

  def place_block(self):
    column = self.choose_action()
    return self.board.place_block(column, self.symbol)

  def post_evaluation_hook(self):
    self.exploration_rate_percentage -= self.exploration_decrease_rate
    print(f'exploration rate: {self.exploration_rate_percentage}%')
    done = self.game.game_finished
    if done:
      is_winner = self.game.winner == self.symbol
      self.reward = 10 if is_winner else -10
    else:
      self.reward = 0
    self.prev_state = self.current_state
    self.current_state = self.board.encode_board(self)
    print(f'prev_state: {self.prev_state}')
    print(f'current_state: {self.current_state}')
    self.replay_memory.append(
      [
        self.prev_state, # last state
        self.action,
        self.reward,
        self.current_state, # new state
        done
      ]
    )