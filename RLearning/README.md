## Lifecycle
1. Agent observes state
2. Agent chooses action
3. Agent takes action
4. State changes
5. Agent receives reward (maybe) & Q-table is updated

### Agent observes state
Agent has access to the connect four grid.

### Agent chooses action
Agent chooses a column to drop a piece into. This is either a random choice or a choice based on the Q-table. In state S, the expected reward for taking action A is Q(S,A).
```
  Q(s,a) = r + x * max(Q(s',a'))
```
Where:
- r is the reward for taking action a in state s (initially zero for all states, but will be updated once the environment has been explored)
- x is the discount factor (0 <= x <= 1). This is used to balance immediate and future reward. If x is close to 0, the agent will be short-sighted and only care about immediate reward. If x is close to 1, the agent will be far-sighted and care about future reward.
- max(Q(s',a')) is the maximum expected reward for any action a' in the new state s'. This is the estimated reward for the best possible action in the new state. (also initialised to zero)

### Agent takes action
Agent drops a piece into the chosen column.

### State changes
The grid is updated

### Agent receives reward (maybe) & Q-table is updated
If the agent has won, the reward is 5. If the agent has lost, the reward is -1. If the agent has drawn, the reward is -5. If the game is still in progress, the reward is 0. The Q-table is updated using the formula above.


