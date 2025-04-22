import pygame
import time
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
        self.is_ghost = False
        self.ghost_timer = 0
        self.ghost_duration = 2000  # Duration in milliseconds (2 seconds)
        self.visible = True  # For flashing effect during ghost state
        self.flash_interval = 100  # Flash interval in milliseconds
    
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
        
        # Update ghost state if active
        if self.is_ghost:
            current_time = pygame.time.get_ticks()
            
            # Update visibility for flashing effect
            if current_time % (self.flash_interval * 2) < self.flash_interval:
                self.visible = True
            else:
                self.visible = False
                
            # Check if ghost state should end
            if current_time - self.ghost_timer >= self.ghost_duration:
                self.exit_ghost_state()
    
    def draw(self, screen):
        """Draw the player on the screen"""
        if not self.is_ghost or self.visible:
            pygame.draw.rect(screen, self.color, self.rect)
    
    def shoot(self):
        """Create a new projectile"""
        projectile_x = self.x + self.width
        projectile_y = self.y + self.height // 2
        new_projectile = Projectile(projectile_x, projectile_y, self.game)
        self.game.projectiles.append(new_projectile)
        
    def enter_ghost_state(self):
        """Enter ghost state where player is immune to collisions"""
        self.is_ghost = True
        self.ghost_timer = pygame.time.get_ticks()
        self.visible = True
    
    def exit_ghost_state(self):
        """Exit ghost state"""
        self.is_ghost = False
        self.visible = True
