import pygame
import random

class Enemy:
    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.speed = random.uniform(1.5, 3.0)  # Random speed for variety
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 0, 0)  # Red color for enemies
    
    def update(self):
        """Update enemy position"""
        self.x -= self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Remove enemy if it goes off screen
        if self.x + self.width < 0:
            self.game.enemies.remove(self)
    
    def draw(self, screen):
        """Draw the enemy on the screen"""
        pygame.draw.rect(screen, self.color, self.rect)
