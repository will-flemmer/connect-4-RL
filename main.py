from connect_four_game import Game, Agent

if __name__ == '__main__':
  red_agent = Agent('RED TEAM', 'red')
  blue_agent = Agent('BLUE TEAM', 'blue')
  lcm = Game(red_agent, blue_agent)
  lcm.start_game()