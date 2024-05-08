# Castle Isolation AI Challenge with Alpha-Beta and Minimax Algorithms

## Objective
This project aims to develop a sophisticated AI capable of mastering Castle Isolation, a strategic board game. The AI leverages advanced algorithms like alpha-beta pruning and minimax to optimize performance against both computer-controlled opponents and other advanced AI systems. This initiative is implemented using Python 3.9, starting from a foundational code framework.

## Overview of Castle Isolation
Castle Isolation is an adaptation of the traditional Isolation game, played on a 9x9 grid with certain squares blocked to create a castle-like structure. This setup restricts movement, adding complexity to the game. Players alternate moves, maneuvering their pieces akin to a chess queen, with the goal of trapping the opponent in such a way that they cannot make a legal move.

## Key Components

### Core Logic (`isolation.py`)
- Includes the primary Board class that governs the game's mechanics.

### AI Development (`castle_isolation.py`)
- The main python file for developing and refining the AI’s strategies using alpha-beta and minimax algorithms.

### Testing Scripts (`player_submission_tests.py` and `test_players.py`)
- Facilitate local testing against various types of players, enhancing the robustness of the AI.

## Development Focus

### Evaluation Functions
- **OpenMoveEvalFn**: Calculates the net number of possible moves for the AI relative to its opponent, crucial for strategic decision-making.
- **CustomEvalFn**: Provides a platform for creating a custom evaluation strategy to further enhance AI performance.

### Strategic Algorithms
- **Minimax Algorithm**: Implement this fundamental game theory technique to determine the optimal move for the AI.
- **Alpha-Beta Pruning**: Enhance the minimax algorithm by incorporating alpha-beta pruning to significantly reduce the number of nodes evaluated in the decision tree.

### Optimization Techniques
- Apply partitioning strategies and memorize evaluation scores to streamline decision processes.
- Identify and prioritize 'killer moves' to enhance tactical advantage.
- Optimize frequently called functions and order nodes strategically to maximize the efficiency of alpha-beta pruning.

## Practical Application
This project showcases the application of complex algorithms in AI to solve intricate problems in game strategy, demonstrating deep analytical skills and advanced programming capabilities.

## Environment Setup
Enables scripts auto-reload to ensure that any changes in the codebase are immediately reflected, aiding continuous development and testing.
