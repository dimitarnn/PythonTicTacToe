## Algorithm Description ##

The algorithm finds the 'optimal' move, given the current board state and assuming optimal play from both players.
Optimal play here means on that each of their turns both players will make the best availble move, with the ultimate
goal of winning the game in as few moves as possible. If a move resulting in a win is not available, the player will
seek to force a draw. Finally if a player can't win and a draw is not possible the player will make the move that will
result in the longest game possible.

The algorithm is implemented inside the `GameLogic` class. The method `get_optimal_move` accepts a board state of
type `Board` and the number of moves already made. It returns a tuple consisting of the game result, in how many moves
the game will end, the row of the optimal move - `row` and the column of the optimal move - `col`.

Game result is `1` if the player whos turn it is can win from the current game state, `0` if the player can achieve
a draw when playing optimally, and `-1` if the player inevitably loses.

The algorithm uses the concepts of Min-Max and game theory to find the optimal move. The algorithm checks future states
achivable after marking a single square (for example at `(row, col)`) from the current state. If at least one of these
states has the game result of `-1` that means the player on the following turn will be presented with a state from which
only a loss is possible. In that case the algorithms chooses the square at `(row, col)` and wins the game.
However if multiple such moves are present, the algorithm chosses the one resulting in the fastest win, or in other
words the one with the lowest number of moves until the game ends.

If none of the next possible states has the result of `-1`, that means a win is not possible from the current state
assuming optimal play, and the algorithm attempts to force a draw. A draw is possible if one of the next states will
be a draw - which means it will have the game result of `0`. If the game will end in a draw the number of moves doesn't
matter, so the algorithm can choose to mark an arbitrary square leading to a state with the result of `0`. 

If none of the next states has the game result of either `-1` or `0` a win or a draw is not possible and the present
state is losing. In such case the algorithm choses the square at `(row, col)` which will lead to the longest game, that is
the state with the largest number of moves until the game ends.

Corner cases are if the game is already over or the number of moves made exceeds the number of squares on the board. In
this case the algorithm checks the game state using the helper method `get_game_result` and returns the found game result,
number of moves made, received as parameter, and `(-1, -1)` for the row and column
