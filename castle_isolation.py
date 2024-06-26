import time
from isolation import Board

class OpenMoveEvalFn:
    def score(self, game, my_player=None):
        """Score the current game state
        Evaluation function that outputs a score equal to how many
        moves are open for AI player on the board minus how many moves
        are open for Opponent's player on the board.

        Note:
            If you think of better evaluation function, do it in CustomEvalFn below.

            Args
                game (Board): The board and game state.
                my_player (Player object): This specifies which player you are.

            Returns:
                float: The current state's score. MyMoves-OppMoves.

            """

        #I am checking to see if the my_player args is given in the function
        if my_player is None:
            raise ValueError("my_player is empty")

        #I am getting the number of moves available for my player,
        # the function get_player_moves is from isolation.py class
        my_moves = len(game.get_player_moves(my_player))

        #I am getting the number of moves available for the opponent,
        # as mentioned above the method get_opponent_moves is from isolation.py class
        opp_moves = len(game.get_opponent_moves(my_player))

        #return the current state's score, by the difference in the number of moves.
        return my_moves - opp_moves



class CustomPlayer:
    # TODO: finish this class!͏󠄂͏️͏󠄌͏󠄎͏︈͏͏󠄁
    """Player that chooses a move using your evaluation function
    and a minimax algorithm with alpha-beta pruning.
    You must finish and test this player to make sure it properly
    uses minimax and alpha-beta to return a good move."""

    def __init__(self, search_depth=4, eval_fn=OpenMoveEvalFn()):
        """Initializes your player.

        if you find yourself with a superior eval function, update the default
        value of `eval_fn` to `CustomEvalFn()`

        Args:
            search_depth (int): The depth to which your agent will search
            eval_fn (function): Evaluation function used by your agent
        """
        self.eval_fn = eval_fn
        self.search_depth = search_depth

    def move(self, game, time_left):
        """Called to determine one move by your agent

        Note:
            1. Do NOT change the name of this 'move' function. We are going to call
            this function directly.
            2. Call alphabeta instead of minimax once implemented.
        Args:
            game (Board): The board and game state.
            time_left (function): Used to determine time left before timeout

        Returns:
            tuple: (int,int): Your best move
        """

        best_move, utility = alphabeta(self, game, time_left, depth=self.search_depth)
        return best_move



    def utility(self, game, my_turn):
        """You can handle special cases here (e.g. endgame)"""

        return self.eval_fn.score(game, self)



def minimax(player, game, time_left, depth, my_turn=True):
    """Implementation of the minimax algorithm.
    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you
            need from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer()).
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """

    # Base case for timeout issues
    if time_left() < 6:
        return None, 0

    # base case of the minmax algorithm
    # This happens when the recursion has reached it's maximum depth in the algo
    # or if there are no legal moves left for the player, hence why I called the get_active_moves() from isolation.py
    # it returns the current position of the player (which is a tuple) and the utility value of the board state.
    if depth == 0 or not game.get_active_moves():
        return game.get_player_position(player), player.utility(game, my_turn)

    #the tuple best_move stores the move that leads to the best outcome possible for the player
    best_move = None

    # this if statement checks if the args my_turn is true, then we run the Max-value algorithm
    # meaning it's going to run for the maximizing player
    if my_turn:

        # val is initialized to negative infinity
        val = float("-inf")

        # This loop iterates over all possible moves for the maximizing player
        for move in game.get_active_moves():

            # addition timeout check within the loop
            if time_left() < 6:
                break
            # we are only extracting new_game variable which is result from the forecasting move in the forecast_move function
            new_game, _, _ = game.forecast_move(move)

            # this is where we make the recursive call to the minvalue function,
            # this is done when we change the my_turn args to false
            # When we change the my_turn to false, in the next recursive iteration, it won't reach this if statement, it will move
            # to the minimizing player, with the else statement.

            _, move_val = minimax(player, new_game, time_left, depth - 1, False)

            # we check to see if the value of move_val is greater than val, it will update the val and best_move with move
            if move_val > val:
                val = move_val
                best_move = move

    # this else statement runs if the args my_turn is false, then we run the min-value algorithm
    # meaning it's going to run for the minimizing player
    else:

        # val is initialized to positive infinity
        val = float("inf")

        # This loop iterates over all possible moves for the minimizing player
        for move in game.get_active_moves():

            # addition timeout check within the loop
            if time_left() < 6:
                break

            # we are only extracting new_game variable which is result from the forecasting move in the forecast_move function
            new_game, _, _ = game.forecast_move(move)

            # this is where we make the recursive call to the maxvalue function,
            # this is done when we change the my_turn args to false
            # When we change the my_turn to true, in the next recursive iteration, it won't reach this else statement, it will move
            # to the maximizing player, with the if statement.

            _, move_val = minimax(player, new_game, time_left, depth - 1, True)

            # we check to see if the value of move_val is greater than val, it will update the val and best_move with move
            if move_val < val:
                val = move_val
                best_move = move

    # we return the best_move and the value based of the minimax algo
    return best_move, val

def alphabeta(player, game, time_left, depth, alpha=float("-inf"), beta=float("inf"), my_turn=True):
    """Implementation of the alphabeta algorithm.

    Args:
        player (CustomPlayer): This is the instantiation of CustomPlayer()
            that represents your agent. It is used to call anything you need
            from the CustomPlayer class (the utility() method, for example,
            or any class variables that belong to CustomPlayer())
        game (Board): A board and game state.
        time_left (function): Used to determine time left before timeout
        depth: Used to track how deep you are in the search tree
        alpha (float): Alpha value for pruning
        beta (float): Beta value for pruning
        my_turn (bool): True if you are computing scores during your turn.

    Returns:
        (tuple, int): best_move, val
    """

    #NOTE: since I am going to be using most of my minimax function here, I won't be explaining line by line
    # Like I did with the minimax function, just so it's not redundant

    if time_left() < 6:
        return None, 0

    # base case of the alphabeta algorithm, same as my minimax algorithm. From the pseudocode of both algos it's same.
    # The explanation for this remains same as minimax algo, so I won't go in depth in explaining.
    if depth == 0 or not game.get_active_moves():
        return game.get_player_position(player), player.utility(game, my_turn)

    # same as minimax algo, the tuple best_move stores the move that leads to the best outcome possible for the player
    best_move = None

    # this if statement runs if the args my_turn is true, then we run the max-value function in the alphabeta algorithm
    if my_turn:

        # val is initialized to negative infinity
        val = float("-inf")

        # This loop iterates over all possible moves for the maximizing player, same as minimax algo
        for move in game.get_active_moves():

            # addition timeout check within the loop
            if time_left() < 6:
                break

            # same as minimax algo, we are getting the result from the forecasting move in the forecast_move function
            new_game, _, _ = game.forecast_move(move)

            # this is where we make the recursive call to the minvalue function for the alphabeta algo,
            # it's Similar to the minimax algo. I won't get in depth of explaining my_turn args to false part
            # only thing different is the inputs for the function, we have additionally alpha and beta

            _, move_val = alphabeta(player, new_game, time_left, depth - 1, alpha, beta, False)

            # we check to see if the value of move_val is greater than val, it will update the val and best_move with move
            if move_val > val:
                val = move_val
                best_move = move

            # after updating the val value, alpha will be set to whatever the max between alpha and val is
            alpha = max(alpha, val)

            # this is the pruning condition for the maximizing player
            if val >= beta:
                return best_move, val

    # this else statement runs if the args my_turn is false, then we run the min-value function in the alphabeta algorithm
    else:

        # val is initialized to positive infinity
        val = float("inf")

        # This loop iterates over all possible moves for the minimizing player, same as minimax algo
        for move in game.get_active_moves():

            # addition timeout check within the loop
            if time_left() < 6:
                break

            # same as minimax algo, we are getting the result from the forecasting move in the forecast_move function
            new_game, _, _ = game.forecast_move(move)

            # this is where we make the recursive call to the maxvalue function of the alphabeta algo,
            #it's Similar to the minimax algo. I won't get in depth of explaining my_turn args to true part
            #only thing different is the inputs for the function, we have additionally alpha and beta

            _, move_val = alphabeta(player, new_game, time_left, depth - 1, alpha, beta, True)

            # we check to see if the value of move_val is greater than val, it will update the val and best_move with move
            if move_val < val:
                val = move_val
                best_move = move

            # after updating the val value, beta will be set to whatever the min between beta and val is
            beta = min(beta, val)

            # this is the pruning condition for the minimizing player
            if val <= alpha:
                return best_move, val

    # we return the best_move and the value based of the alphabeta algo
    return best_move, val
