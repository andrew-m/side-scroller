import pygame
from projectile import Projectile

class Player:
    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.width = 40
        self.height = 30
        self.speed = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (0, 255, 0)  # Green color for player
    
    def update(self):
        """Update player position based on keypresses"""
        keys = pygame.key.get_pressed()
        
        # Vertical movement
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < self.game.height - self.height:
            self.y += self.speed
            
        # Horizontal movement (new)
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < self.game.width - self.width:
            self.x += self.speed
        
        # Update rectangle position
        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self, screen):
        """Draw the player on the screen"""
        pygame.draw.rect(screen, self.color, self.rect)
    
    def shoot(self):
        """Create a new projectile"""
        projectile_x = self.x + self.width
        projectile_y = self.y + self.height // 2
        new_projectile = Projectile(projectile_x, projectile_y, self.game)
        self.game.projectiles.append(new_projectile)
