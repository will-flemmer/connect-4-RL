from . import Agent
from ..board import Board

def test_can_place_block(monkeypatch):
  board = Board()
  agent = Agent('Bob', 'red', board)

  monkeypatch.setattr('builtins.input', lambda _: "1")
  output = agent.place_block()
  assert output == { 'row': 5, 'column': 1 }
  output = agent.place_block()
  assert output == { 'row': 4, 'column': 1 }