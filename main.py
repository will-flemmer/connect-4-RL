from app.lifecycle_manager.lifecycle_manager import LifeCycleManager as Game
from app.agent.agent import Agent

if __name__ == '__main__':
  red_agent = Agent('RED TEAM', 'red')
  blue_agent = Agent('BLUE TEAM', 'blue')
  lcm = Game(red_agent, blue_agent)
  lcm.start_game()