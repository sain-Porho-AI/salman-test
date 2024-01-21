import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
width, height = 800, 600
fps = 30
clock = pygame.time.Clock()

# Colors
water_color = (0, 0, 255)

# Particle class
class WaterParticle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill(water_color)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self):
        # Move the particle downward
        self.rect.y += 2  # Adjust the flow speed

        # Reset the particle position when it goes below the screen
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = random.randint(0, width - 5)

# Create the screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Flowing Vertical River Animation')

# Create a sprite group for water particles
water_particles = pygame.sprite.Group()

# Create initial water particles
for _ in range(100):
    x = random.randint(0, width - 5)
    y = random.randint(0, height - 5)
    particle = WaterParticle(x, y)
    water_particles.add(particle)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Update water particles
        water_particles.update()

        # Draw the river and water particles
        screen.fill((135, 206, 250))  # Fill the screen with light blue for the sky
        pygame.draw.rect(screen, (0, 128, 255), (width // 2 - 25, 0, 50, height))  # Draw the river

        water_particles.draw(screen)

        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()
