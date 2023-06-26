## Lifecycle
1. Agent observes state
2. Agent chooses action
3. Agent takes action
4. State changes
5. Agent receives reward (maybe) & Q-table is updated

### Agent observes state
Agent has access to the connect four grid.

### Agent chooses action
Agent chooses a column to drop a piece into. This is either a random choice or a choice based on the Q-function. In state S, the expected reward for taking action A is Q(S,A). The Q-Function is an approximation of the expected reward for taking action A in state S. The Q-Function is updated using gradient descent at the end of every turn (in the `post_evaluation_hook`).


### Agent takes action
Agent drops a piece into the chosen column.

### State changes
The grid is updated

### Agent receives reward (maybe) & Q-table is updated
If the agent has won, the reward is 5. If the agent has lost, the reward is -1. If the agent has drawn, the reward is -5. If the game is still in progress, the reward is 0. The Q-table is updated using the formula above.


