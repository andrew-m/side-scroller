import pytest
import pygame
from player import Player
from tests.conftest import MockGame

class TestPlayer:
    def test_player_initialization(self):
        """Test that player is initialized with correct attributes"""
        game = MockGame()
        player = Player(50, 300, game)
        
        assert player.x == 50
        assert player.y == 300
        assert player.width == 40
        assert player.height == 30
        assert player.speed == 5
    
    def test_player_movement_up(self, mock_pygame_key_module):
        """Test that player moves up when up arrow is pressed"""
        game = MockGame()
        player = Player(50, 300, game)
        
        # Mock up arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_UP: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should move up by speed amount
        assert player.y == 300 - player.speed
        assert player.rect.y == player.y
    
    def test_player_movement_down(self, mock_pygame_key_module):
        """Test that player moves down when down arrow is pressed"""
        game = MockGame()
        player = Player(50, 300, game)
        
        # Mock down arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_DOWN: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should move down by speed amount
        assert player.y == 300 + player.speed
        assert player.rect.y == player.y
    
    def test_player_movement_boundary_top(self, mock_pygame_key_module):
        """Test that player cannot move above the screen"""
        game = MockGame()
        player = Player(50, 0, game)  # Start at top edge
        
        # Mock up arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_UP: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should not move up beyond top boundary
        assert player.y == 0
        assert player.rect.y == player.y
    
    def test_player_movement_boundary_bottom(self, mock_pygame_key_module):
        """Test that player cannot move below the screen"""
        game = MockGame()
        player = Player(50, 300, game)  # Not at bottom edge yet
        
        # Set player at bottom edge
        player.y = game.height - player.height
        player.rect.y = player.y
        
        # Mock down arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_DOWN: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should not move beyond bottom boundary
        assert player.y == game.height - player.height
        assert player.rect.y == player.y
    
    def test_player_movement_left(self, mock_pygame_key_module):
        """Test that player moves left when left arrow is pressed"""
        game = MockGame()
        player = Player(50, 300, game)
        
        # Mock left arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_LEFT: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should move left by speed amount
        assert player.x == 50 - player.speed
        assert player.rect.x == player.x
    
    def test_player_movement_right(self, mock_pygame_key_module):
        """Test that player moves right when right arrow is pressed"""
        game = MockGame()
        player = Player(50, 300, game)
        
        # Mock right arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_RIGHT: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should move right by speed amount
        assert player.x == 50 + player.speed
        assert player.rect.x == player.x
    
    def test_player_movement_boundary_left(self, mock_pygame_key_module):
        """Test that player cannot move beyond left edge of the screen"""
        game = MockGame()
        player = Player(0, 300, game)  # Start at left edge
        
        # Mock left arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_LEFT: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should not move beyond left boundary
        assert player.x == 0
        assert player.rect.x == player.x
    
    def test_player_movement_boundary_right(self, mock_pygame_key_module):
        """Test that player cannot move beyond right edge of the screen"""
        game = MockGame()
        player = Player(300, 300, game)  # Not at right edge yet
        
        # Set player at right edge
        player.x = game.width - player.width
        player.rect.x = player.x
        
        # Mock right arrow key press
        mock_pygame_key_module.keys_pressed = {pygame.K_RIGHT: True}
        
        # Call update to process the key press
        player.update()
        
        # Player should not move beyond right boundary
        assert player.x == game.width - player.width
        assert player.rect.x == player.x
    
    def test_player_shoot(self):
        """Test that player can shoot projectiles"""
        game = MockGame()
        player = Player(50, 300, game)
        
        # No projectiles initially
        assert len(game.projectiles) == 0
        
        # Player shoots
        player.shoot()
        
        # A projectile should be created
        assert len(game.projectiles) == 1
        
        # Check projectile properties
        projectile = game.projectiles[0]
        assert projectile.x == player.x + player.width
        assert projectile.y == player.y + player.height // 2
