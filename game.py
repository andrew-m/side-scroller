import pygame
import sys
from player import Player
from enemy import Enemy
from projectile import Projectile
import random

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Side-Scrolling Shooter")
        
        # Game settings
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True
        self.game_over = False
        
        # Game elements
        self.player = Player(50, self.height // 2, self)
        self.enemies = []
        self.projectiles = []
        
        # Game variables
        self.score = 0
        self.lives = 3
        self.enemy_spawn_rate = 60  # frames between enemy spawns
        self.spawn_counter = 0
        
        # Wave variables
        self.current_wave = 1
        self.wave_enemies_spawned = 0
        self.wave_enemies_required = self.calculate_wave_enemies(self.current_wave)
        self.wave_completed = False
        self.wave_transition = False
        self.wave_message_timer = 0
        self.wave_message_duration = 1000  # 1 second in milliseconds
        
        # Font for text display
        self.font = pygame.font.SysFont(None, 36)
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            
            if not self.game_over:
                self.update()
            
            self.render()
            self.clock.tick(self.FPS)
        
        pygame.quit()
        sys.exit()
    
    def handle_events(self):
        """Handle player input"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            # Restart game if it's game over
            if self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.reset_game()
                elif event.key == pygame.K_q:
                    self.running = False
            
            # Shooting
            if not self.game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.player.shoot()
        
    def update(self):
        """Update game state"""
        # Check for wave transition
        if self.wave_transition:
            current_time = pygame.time.get_ticks()
            if current_time - self.wave_message_timer >= self.wave_message_duration:
                self.start_next_wave()
            return
        
        # Check if wave is completed
        if self.wave_enemies_spawned >= self.wave_enemies_required and len(self.enemies) == 0:
            self.complete_wave()
            return
        
        # Update player
        self.player.update()
        
        # Spawn enemies - only if we haven't reached the wave limit
        if self.wave_enemies_spawned < self.wave_enemies_required:
            self.spawn_counter += 1
            if self.spawn_counter >= self.enemy_spawn_rate:
                y_pos = random.randint(50, self.height - 50)
                self.enemies.append(Enemy(self.width, y_pos, self))
                self.wave_enemies_spawned += 1
                self.spawn_counter = 0
        
        # Update enemies
        for enemy in self.enemies[:]: 
            enemy.update()
            
            # Check for collisions with player
            if self.check_collision(enemy.rect, self.player.rect):
                # Only destroy the enemy and affect player if not in ghost state
                if not self.player.is_ghost:
                    self.enemies.remove(enemy)
                    self.lives -= 1
                    # Enter ghost state when hit
                    self.player.enter_ghost_state()
                    if self.lives <= 0:
                        self.game_over = True
        
        # Update projectiles
        for projectile in self.projectiles[:]:
            projectile.update()
            
            # Check for collisions with enemies
            for enemy in self.enemies[:]:
                if self.check_collision(projectile.rect, enemy.rect):
                    self.projectiles.remove(projectile)
                    self.enemies.remove(enemy)
                    self.score += 10
                    break
    
    def render(self):
        """Render game elements"""
        self.screen.fill(self.BLACK)
        
        # Draw game elements
        self.player.draw(self.screen)
        
        for enemy in self.enemies:
            enemy.draw(self.screen)
        
        for projectile in self.projectiles:
            projectile.draw(self.screen)
        
        # Draw HUD
        self.draw_hud()
        
        # Draw game over screen
        if self.game_over:
            self.draw_game_over()
        
        # Draw wave transition message
        if self.wave_transition:
            self.draw_wave_message()
        
        pygame.display.flip()
    
    def draw_hud(self):
        """Draw score, lives, and wave info"""
        score_text = self.font.render(f"Score: {self.score}", True, self.WHITE)
        lives_text = self.font.render(f"Lives: {self.lives}", True, self.WHITE)
        wave_text = self.font.render(f"Wave: {self.current_wave}", True, self.WHITE)
        
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(lives_text, (10, 50))
        self.screen.blit(wave_text, (10, 90))
    
    def draw_game_over(self):
        """Draw game over screen"""
        game_over_text = self.font.render("GAME OVER", True, self.RED)
        restart_text = self.font.render("Press R to Restart or Q to Quit", True, self.WHITE)
        
        self.screen.blit(game_over_text, (self.width // 2 - game_over_text.get_width() // 2, 
                                        self.height // 2 - game_over_text.get_height() // 2))
        self.screen.blit(restart_text, (self.width // 2 - restart_text.get_width() // 2, 
                                      self.height // 2 + 50))
    
    def check_collision(self, rect1, rect2):
        """Check if two rectangles collide"""
        return rect1.colliderect(rect2)
    
    def calculate_wave_enemies(self, wave_number):
        """Calculate number of enemies for a given wave"""
        return 30 + (wave_number - 1) * 10
    
    def complete_wave(self):
        """Handle wave completion"""
        self.wave_completed = True
        self.wave_transition = True
        self.wave_message_timer = pygame.time.get_ticks()
    
    def start_next_wave(self):
        """Start the next wave"""
        self.current_wave += 1
        self.wave_enemies_spawned = 0
        self.wave_enemies_required = self.calculate_wave_enemies(self.current_wave)
        self.wave_completed = False
        self.wave_transition = False
    
    def draw_wave_message(self):
        """Draw wave transition message"""
        message = f"Wave {self.current_wave} Cleared!"
        next_wave_message = f"Get Ready, Wave {self.current_wave + 1}!"
        
        wave_text = self.font.render(message, True, self.WHITE)
        next_wave_text = self.font.render(next_wave_message, True, self.WHITE)
        
        # Center the messages on screen
        wave_text_rect = wave_text.get_rect(center=(self.width // 2, self.height // 2 - 30))
        next_wave_text_rect = next_wave_text.get_rect(center=(self.width // 2, self.height // 2 + 30))
        
        self.screen.blit(wave_text, wave_text_rect)
        self.screen.blit(next_wave_text, next_wave_text_rect)
    
    def reset_game(self):
        """Reset the game state"""
        self.player = Player(50, self.height // 2, self)
        self.enemies = []
        self.projectiles = []
        self.score = 0
        self.lives = 3
        self.game_over = False
        self.spawn_counter = 0
        # Reset wave variables
        self.current_wave = 1
        self.wave_enemies_spawned = 0
        self.wave_enemies_required = self.calculate_wave_enemies(self.current_wave)
        self.wave_completed = False
        self.wave_transition = False
        # Ensure player is not in ghost state after reset
        self.player.is_ghost = False
        self.player.visible = True
