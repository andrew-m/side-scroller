import pygame

class Projectile:
    def __init__(self, x, y, game):
        self.game = game
        self.x = x
        self.y = y
        self.width = 10
        self.height = 5
        self.speed = 7
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color = (255, 255, 0)  # Yellow color for projectiles
    
    def update(self):
        """Update projectile position"""
        self.x += self.speed
        self.rect.x = self.x
        self.rect.y = self.y
        
        # Remove projectile if it goes off screen
        if self.x > self.game.width:
            self.game.projectiles.remove(self)
    
    def draw(self, screen):
        """Draw the projectile on the screen"""
        pygame.draw.rect(screen, self.color, self.rect)
