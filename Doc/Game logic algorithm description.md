## Game Logic

This sections describes how the computer simulates the opponent selecting the next move on the board. It must be 
noted that there are many implementations available. For the sake of simplicity the **Min-Max 
Algorithm** was chosen.

_________________________________________________________________________________________________
### Concept

The algorithm shall find what the 'optimal' play is at a given state of the board.
The definition of optimal play is the following:

1. Win the game in as few moves as possible
2. If a win is not possible then force a draw
3. If a draw is not possible then try to prolong the game as much as possible

*Note: The algorithm assumes the opponent is also going to play optimally*
_________________________________________________________________________________________________
### Input Data

- Board state
- Number of moves already made

_________________________________________________________________________________________________
### Output Data

- Game result
- Number of moves made when the game ends, if both players play optimally
from the current board state
- The row of the optimal move
- The column of the optimal move

#### Game result can be either `1`, `0` or `-1`:
* `1` means that the player making the current move can win from the current game state,
regardless of the opponents' moves
* `0` means that the player making the current move can achieve a draw at best if the opponent
plays optimally
* `-1` means that the player making the current move will inevitably lose the game if the
opponent plays optimally

_________________________________________________________________________________________________
### Algorithm

The algorithm uses the concepts of Min-Max and game theory to find the optimal move. It checks
all future states, achievable from the current state after marking a single square
(*for example at `(row, col)`*). The game results of these future states are calculated recursively,
using the same logic.

![TicTacToe Diagram 1](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_algorithm_diagram_1.png)

* If at least one of these states has the game result of `-1` that means the player on the 
following turn will be presented with a state from which only a loss is possible. In that case 
the algorithms chooses the square at `(row, col)` and eventually wins the game.

![TicTacToe Diagram 2](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_algorithm_diagram_2.png)

* However if multiple such moves are present, the algorithm chooses the one resulting in the 
fastest win, or in other words the one with the lowest number of moves made when the game ends.

![TicTacToe Diagram 2](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_algorithm_diagram_3.png)

* If a win is not possible from the current state the algorithm attempts to force a draw. A draw 
is possible if one of the next states will have the game result of `0`. If the game will 
end in a draw the number of moves made doesn't matter, so the algorithm can choose to mark 
an arbitrary square leading to a state with the game result of `0`.

![TicTacToe Diagram 4](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_algorithm_diagram_4.png)

* If from the current state all possible next states have the game result of `1` it means that the player on the
following turn will win the game, no matter which square the algorithm chooses. In other words from the current state
neither a win, nor draw is achievable, so the algorithm should mark the square at `(row, col)` that will 
result in the longest game, and that is the square leading to the state with the largest number of moves made when the game ends.

![TicTacToe Diagram 5](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_algorithm_diagram_5.png)

* Corner cases are if the game is already over or the number of moves made exceeds the number of 
squares on the board. In this case the algorithm checks the game state and returns the game result,
number of moves made received as parameter, and `(-1, -1)` for the row and column.

![TicTacToe Diagram 6](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_algorithm_diagram_6.png)

_________________________________________________________________________________________________
**A diagram showing the possible board states, achievable from a given game state, and the game result of each of these states if both players play optimally:**

![TicTacToe diagram](https://github.com/dimitarnn/PythonTicTacToe/blob/master/Doc/TicTacToe_possibility_tree_png.png)

