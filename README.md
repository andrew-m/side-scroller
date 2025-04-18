# Side-Scrolling Shooter Game

A simple 2D side-scrolling shoot-em-up game built with Python and Pygame. The player controls a spaceship that moves vertically, shooting projectiles to destroy incoming enemy blobs.

## Features

- Player controls (up/down movement, shooting)
- Enemy blob spawning and movement
- Projectile shooting and collision detection
- Score tracking and lives system
- Game over and restart functionality

## Requirements

- Python 3.x
- Pygame 2.5.2

## Installation

1. Ensure you have Python 3.x installed
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## How to Run

Execute the main.py file:

```
python main.py
```

## Controls

- **Arrow Up**: Move spaceship up
- **Arrow Down**: Move spaceship down
- **Spacebar**: Shoot projectiles
- **R**: Restart game (after game over)
- **Q**: Quit game (after game over)

## Game Structure

- **main.py**: Entry point for the game
- **game.py**: Contains the Game class that manages the game loop and state
- **player.py**: Implements the Player class
- **enemy.py**: Implements the Enemy (blob) class
- **projectile.py**: Implements the Projectile class

## Future Improvements

- Add sprite graphics instead of simple shapes
- Add sound effects and background music
- Implement different enemy types with varying behaviors
- Add power-ups and special weapons
- Implement scrolling background
