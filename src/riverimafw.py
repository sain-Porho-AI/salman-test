import pygame
import numpy as np

# Set up Pygame
pygame.init()

# Define parameters
width, height = 800, 600
sky_blue = (135, 206, 250)  # RGB values for sky blue
river_blue = (70, 130, 180)  # RGB values for river blue

# Set up Pygame display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wider Vertical River Animation")

# Function to create moving water effect
def generate_river(frame):
    river_width = width // 2  # Adjust the river width as needed
    river_surface = pygame.Surface((river_width, height), pygame.SRCALPHA)
    river_surface.fill((0, 0, 0, 0))  # Set alpha to 0 for transparency

    # Generate sine wave for water movement
    wave_amplitude = 10
    wave_frequency = 0.1
    x_values = np.sin(np.linspace(0, 2 * np.pi * wave_frequency, height)) * wave_amplitude + river_width // 2

    # Draw wider river with moving water
    pygame.draw.polygon(river_surface, river_blue, [(x, y) for x, y in zip(x_values, range(height))], 0)

    return river_surface

# Generate frames for the GIF
num_frames = 60
frames = [generate_river(frame) for frame in range(num_frames)]

# Save the GIF
pygame.image.save(frames[0], "wider_vertical_river_animation.jpg")

# Close Pygame
pygame.quit()
