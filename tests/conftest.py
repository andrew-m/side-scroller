import pytest
import pygame
import sys

# Initialize pygame for testing
pygame.init()

# Mock pygame.key.get_pressed to avoid dependency on actual keyboard input
class MockKeys:
    def __init__(self, keys_pressed=None):
        self.keys_pressed = keys_pressed or {}
    
    def __getitem__(self, key):
        return self.keys_pressed.get(key, False)

@pytest.fixture
def mock_pygame_key_module(monkeypatch):
    """Fixture to mock pygame.key.get_pressed"""
    mock_keys = MockKeys()
    
    def mock_get_pressed():
        return mock_keys
    
    monkeypatch.setattr(pygame.key, 'get_pressed', mock_get_pressed)
    return mock_keys

# A fixture to mock pygame initialization and display functions
@pytest.fixture
def mock_pygame(monkeypatch):
    """Fixture to mock pygame functions"""
    monkeypatch.setattr(pygame, 'init', lambda: None)
    monkeypatch.setattr(pygame.display, 'set_caption', lambda x: None)
    monkeypatch.setattr(pygame.display, 'set_mode', lambda x: pygame.Surface((800, 600)))
    monkeypatch.setattr(pygame.font, 'SysFont', lambda name, size: pygame.font.Font(None, size))
    return monkeypatch

# Mock game class for testing
class MockGame:
    """A simplified game class for testing"""
    def __init__(self):
        self.width = 800
        self.height = 600
        self.projectiles = []
        self.enemies = []
        self.score = 0
        self.lives = 3
        self.game_over = False
    
    def check_collision(self, rect1, rect2):
        """Simplified collision detection for testing"""
        return rect1.colliderect(rect2)
        
    def remove_enemy(self, enemy):
        """Helper method to remove an enemy properly in tests"""
        if enemy in self.enemies:
            self.enemies.remove(enemy)
            
    def remove_projectile(self, projectile):
        """Helper method to remove a projectile properly in tests"""
        if projectile in self.projectiles:
            self.projectiles.remove(projectile)
