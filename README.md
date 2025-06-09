# ♟️ Checkers
**♟️ Checkers** - A Python-based Checkers simulator featuring an intelligent AI that makes strategic moves using the Minimax algorithm with Alpha-Beta pruning for optimal decision-making. The game includes a real-time graphical board interface powered by Pygame, delivering an interactive and engaging experience.


***
## Technologies
![Static Badge](https://img.shields.io/badge/python-3.12%2B-blue)
![Static Badge](https://img.shields.io/badge/library-pygame-green)
![Platform](https://img.shields.io/badge/Platform-Windows_|_Linux_|_MacOS-lightgrey?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0-brightgreen?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)

<a name="features"><a/>
## Features
#### AI & Algorithmic Logic:
 - **Heuristic Evaluation** – Scores board states based on piece positions and game dynamics.

 - **Variable Depth Search** – Dynamically adjusts search depth for faster and smarter move selection.

 - **Minimax Algorithm** – Explores future game states to determine the most strategic move.

 - **Alpha-Beta Pruning** – Speeds up decision-making by pruning irrelevant branches in the search tree.

 - **Hash Map Optimization** – Caches game states to reduce redundant computations and improve performance.

#### Gameplay & Rules:
- **Standard Checkers Mechanics** – Diagonal movement and capturing via jumps over opponent pieces.

- **Two Game Modes** – Choose between mandatory or optional captures.

- **King Promotion** – Pieces reaching the opponent’s back row are promoted to "kings" with backward movement.

- **Multi-Jump Support** – Chain multiple captures in a single turn when available.

#### Performance: 
- **Move Time Limit** – AI computes a move within 5 seconds.


***
## Contents
1. [Features](#features)
2. [Dependencies](#dependencies)
3. [Getting Started](#start)
4. [Functionalities](#functionalities)
4. [License](#license)
5. [Contact](#contact)

***
<a name="dependencies"><a/>
## Dependencies
In order to run this project properly you need to make sure that you have installed:
1. **Python programming language - Version 3.12 and above**: you can download python [here](https://www.python.org/downloads/).
2. **PyGame**: free and open-source cross-platform library for the development of multimedia applications like video games using Python.
4. **Python IDE or text editor** (optional): you can use either [PyCharm](https://www.jetbrains.com/pycharm/) or [Visual Studio Code](https://code.visualstudio.com/)
5. **Git** (optional): if you want to download this project and contribute to it

***
<a name="start"><a/>
## Getting Started

1. **Clone the Repository**:
   
    Open a terminal and run the following command to clone the repository:


   ```bash
   https://github.com/vasicm4/checkers.git
    ```
    Alternatively, download the repository as a ZIP file and extract it.

2. **Installation of additional libraries and dependencies**:
    - Open terminal or command prompt based on operating system
    - Navigate to the folder where the repository is located
    - Insert `pip install -r requirements.txt` in terminal
    - Alternatively you can execute `pip install pygame`

3. **Run the program**:
    To start the program type `python src/Menu.py` in your terminal


4. **Choose a game mode and enjoy the game!**

    
***
<a name="functionalities"><a/>
## Functionalities

The Checkers AI game is built on standard checkers rules, with players alternating turns and moving pieces diagonally. The AI determines the optimal move using the Minimax algorithm enhanced with Alpha-Beta Pruning, while dynamically adjusting its search depth to maintain high performance.

- **Game Initialization**
  - Sets up the 8x8 board and places 12 pieces per player.
  - Offers two game rule modes: **mandatory** or **optional captures**.

-  **User Turn**
  - Displays current board in the console with clearly marked positions.
  - Shows all **valid moves** and lets the player select one easily.

-  **AI Turn**
  - Runs the **Minimax algorithm** to simulate possible future states.
  - Uses **Heuristic Evaluation** to score each potential outcome.
  - Applies **Alpha-Beta Pruning** to skip unnecessary evaluations and stay efficient.
  - Adapts **search depth dynamically** using the Variable Depth Search engine.
  - Speeds up decision-making using a **Hash Map cache** of already-seen states.
  - Picks the best move within **5 seconds**

-  **Game Rules Logic**
  - Handles **king promotions**, **multi-jump sequences**, and legal movement.
  - Updates board after each move and switches turns.

-  **GUI**
  - Redraws the board after every move.
  - Highlights moves, recent plays, and available options for the player.
  - Ensures a **smooth, clear, and intuitive** user experience.

-  **Endgame Detection**
  - Checks if a player has run out of pieces.
  - Declares the winner and ends the game.
---

###  Core AI Algorithms Explained

The AI in this Checkers game leverages the Minimax algorithm with Alpha-Beta pruning for efficient and strategic decision-making. It also incorporates variable search depth, heuristic evaluation, and hash map-based board state caching to boost performance and reduce computation time.

####  **Minimax Algorithm**
- Simulates all possible future game states by alternating player turns.
- Assumes both players play optimally — one tries to **maximize** their advantage, the other to **minimize** it.
- Chooses the move that leads to the **best worst-case outcome**.

####  **Alpha-Beta Pruning**
- An optimization of the Minimax algorithm that skips unnecessary calculations.
- "Prunes" parts of the search tree that won’t affect the final decision.
- reatly reduces the number of nodes evaluated, making the AI much faster.

####  **Heuristic Evaluation**
- Assigns a score to each board state to estimate how favorable it is.
- Factors in things like number of pieces, king status, positioning, and control of the board.
- Guides the AI toward smart moves even if the game isn't fully simulated.

####  **Variable Depth Search**
- Adjusts how many moves ahead the AI looks, depending on the situation.
- In simple states, it searches deeper; in complex ones, it searches shallower to stay within the time limit.
- Balances accuracy and performance for consistent move decisions.

####  **Hash Map Optimization**
- Caches already-evaluated board states to avoid recalculating them.
- Saves time and prevents repeating expensive computations.
- Useful in games with recurring patterns or symmetrical positions.


 The result is an AI that plays smart, adapts to changing game scenarios, and makes consistently optimized decisions!

***
<a name="license"><a/>
## ⚖ License
This project is licensed under the [MIT License](./LICENSE). See the [LICENSE](./LICENSE) file for details.

***
<a name="contact"><a/>
##  Contact me

 - **Email**: [vasicmaksim4@gmail.com](mailto:vasicmaksim4@gmail.com)
 - **Github**: [vasicm4](https://github.com/vasicm4)
 - **Linkedin**: [Maksim Vasic](https://rs.linkedin.com/in/maksim-vasi%C4%87-514b11327)
***
