import pygame

pygame.init()
wn = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

def draw_gradient_river(x, y, width, height, color):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    for i in range(height):
        alpha = int(255 * (1 - abs((height / 2 - i) / (height / 2))))
        pygame.draw.line(surface, (color[0], color[1], color[2], alpha), (0, i), (width, i), 1)
    wn.blit(surface, (x, y))

def draw_flow_animation(x, y, width, height, color, speed):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    time_passed = pygame.time.get_ticks() // speed
    for i in range(height):
        alpha = int(255 * (1 - abs((height / 2 - i + time_passed) / (height / 2))))
        pygame.draw.line(surface, (color[0], color[1], color[2], alpha), (0, i), (width, i), 1)
    wn.blit(surface, (x, y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    river_color = (100, 200, 255)
    darker_river_color = (70, 130, 180, 255)  # Add alpha value to the color
    river_width = 350  # Adjust the width as needed

    wn.fill((255, 255, 255))  # Fill background with white

    # Draw the gradient river at the current position
    draw_gradient_river(300 - river_width // 2, 0, river_width, 600, darker_river_color)

    # Draw the original river on top
    pygame.draw.rect(wn, river_color, (300 - river_width // 2, 0, river_width, 600))

    # Add flowing water animation
    draw_flow_animation(300 - river_width // 2, 0, river_width, 600, (255, 255, 255), 100)

    pygame.display.update()
    clock.tick(30)  # Adjust the frame rate as needed
