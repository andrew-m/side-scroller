Game Specification: Side-Scrolling Shoot-Em-Up
1. Game Overview

The game is a simple 2D side-scrolling shoot-em-up where the player controls a spaceship that moves horizontally across the screen. The objective is to shoot and destroy blobs that appear from the right side of the screen while avoiding collisions with them. The game will feature basic mechanics, including player movement, shooting, enemy spawning, and collision detection.
2. Game Mechanics
2.1 Player Controls

    Movement: The player can move the spaceship up and down using the arrow keys.
    Shooting: The player can shoot projectiles by pressing the spacebar.

2.2 Enemies

    Blobs: Blobs will spawn from the right side of the screen and move towards the left. They will have simple linear movement.

2.3 Projectiles

    Player Projectiles: The spaceship can shoot projectiles that move horizontally from left to right. These projectiles will destroy blobs upon collision.

2.4 Collision Detection

    Player-Blob Collision: If the player's spaceship collides with a blob, the blob is destroyed and the player loses a life. After collision, the player enters a 'ghost state' for 2 seconds, during which they flash (appearing and disappearing rapidly) and are immune to collisions with other blobs. While in ghost state, blobs that collide with the player pass through harmlessly and are not destroyed.
    Projectile-Blob Collision: If a projectile collides with a blob, the blob is destroyed, and the player earns points.

3. Game Elements
3.1 Player

    Sprite: A simple spaceship image.
    Movement Speed: Adjustable speed for vertical movement.
    Lives: The player starts with a set number of lives.

3.2 Enemies

    Sprite: Simple blob images.
    Spawn Rate: Adjustable rate at which blobs appear.
    Movement Speed: Adjustable speed for blobs moving from right to left.

3.3 Projectiles

    Sprite: Simple projectile image.
    Speed: Adjustable speed for projectiles moving from left to right.

3.4 Score

    Display: The player's score will be displayed on the screen.
    Points: Points are awarded for each blob destroyed.

4. Game Loop
4.1 Initialization

    Initialize Pygame and set up the game window.
    Load all necessary assets (sprites, sounds, etc.).
    Initialize game variables (player position, score, lives, etc.).

4.2 Main Loop

    Event Handling: Handle player input for movement and shooting.
    Update: Update the positions of the player, projectiles, and blobs. Check for collisions and update the score and lives accordingly.
    Render: Draw all game elements on the screen.
    Frame Rate: Control the frame rate to ensure smooth gameplay.

4.3 Game Over

    Display a game over screen when the player loses all lives.
    Provide an option to restart the game or quit.

5. Assets

    Player Sprite: A simple image of a spaceship.
    Blob Sprite: Simple images of blobs.
    Projectile Sprite: A simple image of a projectile.
    Background: A simple scrolling background image (optional).
    Sounds: Sound effects for shooting, blob destruction, and game over (optional).

6. Code Structure
6.1 Main File

    Initialize Pygame and set up the game window.
    Load assets and initialize game variables.
    Implement the main game loop.

6.2 Player Class

    Handle player movement and shooting.
    Draw the player on the screen.

6.3 Blob Class

    Handle blob spawning and movement.
    Draw blobs on the screen.

6.4 Projectile Class

    Handle projectile movement.
    Draw projectiles on the screen.

6.5 Collision Detection

    Implement functions to check for collisions between the player, blobs, and projectiles.

6.6 Score and Lives

    Implement functions to update and display the player's score and lives.
