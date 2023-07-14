from RLearning.rl_agent import RLAgent
from connect_four_game import Game


COLUMN_COUNT = 7 # normally 7
ROW_COUNT = 6 # normally 6

# An episode is a full game
TRAIN_EPISODES = 3
TEST_EPISODES = 100

"""
  agent is peristed across games
"""

if __name__ == '__main__':
  red_rl_agent = RLAgent('red')
  blue_rl_agent = RLAgent('blue')
  for episode in range(TRAIN_EPISODES):
    game = Game(red_rl_agent, blue_rl_agent, row_count=ROW_COUNT, column_count=COLUMN_COUNT)
    game.start_game()
  