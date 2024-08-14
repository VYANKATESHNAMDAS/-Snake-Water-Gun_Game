# Snake-Water-Gun Game

This repository contains a simple command-line implementation of the Snake-Water-Gun game in Python. The game is played between the user and the computer in a best-of-five format.

## How to Play

- The user chooses between Snake (s), Water (w), and Gun (g).
- The computer randomly selects one of the three options.
- The winner is determined based on the following rules:
  - Snake drinks Water: Snake wins.
  - Water douses Gun: Water wins.
  - Gun shoots Snake: Gun wins.

## Requirements

- Python 3.x

## Running the Game

1. Clone the repository:

    ```bash
    git clone https://github.com/VYANKATESHNAMDAS/snake-water-gun.git
    ```

2. Navigate to the project directory:

    ```bash
    cd snake-water-gun
    ```

3. Run the game script:

    ```bash
    python snake_water_gun.py
    ```

4. Follow the on-screen prompts to play the game.

## Example Output

```plaintext
Comp turn: Snake (s), Water (w), Gun (g)?
Your turn: Snake (s), Water (w), Gun (g)? s
Computer chose: g
YOU LOSE!
