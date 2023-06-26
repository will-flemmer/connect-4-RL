from RLearning.rl_agent import RLAgent
from app.lifecycle_manager.lifecycle_manager import LifeCycleManager as Game


COLUMN_COUNT = 7 # normally 7
ROW_COUNT = 6 # normally 6
ACTION_COUNT = COLUMN_COUNT


if __name__ == '__main__':
  red_rl_agent = RLAgent('red')
  blue_rl_agent = RLAgent('blue')
  game = Game(red_rl_agent, blue_rl_agent, row_count=ROW_COUNT, column_count=COLUMN_COUNT)
  game.start_game()
  