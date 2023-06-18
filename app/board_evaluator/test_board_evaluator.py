from ..board import Board
from . import BoardEvaluator
from ..agent import Agent

def test_can_spot_a_horizontal_win():
  board = Board()
  red_agent = Agent('Bob', 'red', board)
  blue_agent = Agent('Ted', 'blue', board)
  evaluator = BoardEvaluator(board, red_agent, blue_agent)

  board.grid[0][0] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 0})
  assert result['completed'] == False

  board.grid[0][1] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 1})
  assert result['completed'] == False

  board.grid[0][2] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 2})
  assert result['completed'] == False

  board.grid[0][3] = 'R'
  result = evaluator.evaluate(red_agent, {'row': 0, 'column': 3})
  assert result['completed'] == True
  assert result['winner'] == red_agent

def test_can_spot_a_vertical_win():
  board = Board()
  red_agent = Agent('Bob', 'red', board)
  blue_agent = Agent('Ted', 'blue', board)
  evaluator = BoardEvaluator(board, red_agent, blue_agent)
  board.grid[1][0] = 'B'
  board.grid[2][0] = 'B'
  board.grid[3][0] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 3, 'column': 0})
  assert result['completed'] == False

  board.grid[4][0] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 4, 'column': 0})
  assert result['completed'] == True
  assert result['winner'] == blue_agent

def test_can_spot_a_positive_diagonal_win():
  board = Board()
  red_agent = Agent('Bob', 'red', board)
  blue_agent = Agent('Ted', 'blue', board)
  evaluator = BoardEvaluator(board, red_agent, blue_agent)
  board.grid[1][0] = 'B'
  board.grid[2][1] = 'B'
  board.grid[3][2] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 3, 'column': 2})
  assert result['completed'] == False

  board.grid[4][3] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 4, 'column': 3})
  assert result['completed'] == True
  assert result['winner'] == blue_agent

def test_can_spot_a_negative_diagonal_win():
  board = Board()
  red_agent = Agent('Bob', 'red', board)
  blue_agent = Agent('Ted', 'blue', board)
  evaluator = BoardEvaluator(board, red_agent, blue_agent)
  board.grid[1][3] = 'B'
  board.grid[2][2] = 'B'
  board.grid[3][1] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 3, 'column': 1})
  assert result['completed'] == False

  board.grid[4][0] = 'B'
  result = evaluator.evaluate(blue_agent, {'row': 4, 'column': 0})
  assert result['completed'] == True
  assert result['winner'] == blue_agent