from RLearning.rl_agent import RLAgent
from app.lifecycle_manager.lifecycle_manager import LifeCycleManager as Game

if __name__ == '__main__':
  red_rl_agent = RLAgent('red')
  blue_rl_agent = RLAgent('blue')
  game = Game(red_rl_agent, blue_rl_agent)
  game.start_game()
  