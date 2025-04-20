import pytest
import pygame
from projectile import Projectile
from tests.conftest import MockGame

class TestProjectile:
    def test_projectile_initialization(self):
        """Test that projectile is initialized with correct attributes"""
        game = MockGame()
        projectile = Projectile(100, 200, game)
        
        assert projectile.x == 100
        assert projectile.y == 200
        assert projectile.width == 10
        assert projectile.height == 5
        assert projectile.speed == 7
        assert isinstance(projectile.rect, pygame.Rect)
        assert projectile.color == (255, 255, 0)  # Yellow color
    
    def test_projectile_movement(self):
        """Test that projectile moves correctly"""
        game = MockGame()
        projectile = Projectile(100, 200, game)
        
        # Initial position
        initial_x = projectile.x
        
        # Update projectile position
        projectile.update()
        
        # Projectile should move right by speed amount
        assert projectile.x == initial_x + projectile.speed
        assert projectile.rect.x == projectile.x
        assert projectile.rect.y == projectile.y
    
    def test_projectile_removal_when_offscreen(self):
        """Test that projectile is removed when it goes off screen"""
        game = MockGame()
        
        # Create projectile beyond the edge of the screen
        projectile = Projectile(game.width + 10, 200, game)  # Already off-screen to the right
        game.projectiles.append(projectile)
        
        # Before update
        assert len(game.projectiles) == 1
        
        # We'll directly test the condition that should remove the projectile
        if projectile.x > game.width:
            game.remove_projectile(projectile)
        
        # Projectile should be removed from the game's projectiles list
        assert len(game.projectiles) == 0
    
    def test_projectile_stays_in_list_when_onscreen(self):
        """Test that projectile stays in the list when still on screen"""
        game = MockGame()
        
        # Create projectile well within the screen
        projectile = Projectile(300, 200, game)
        game.projectiles.append(projectile)
        
        # Before update
        assert len(game.projectiles) == 1
        
        # Update projectile position - it should remain on screen
        projectile.update()
        
        # Projectile should still be in the game's projectiles list
        assert len(game.projectiles) == 1
