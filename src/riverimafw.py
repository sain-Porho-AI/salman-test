import pygame

pygame.init()
wn = pygame.display.set_mode((600, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    river_color = (100, 200, 255)
    river_width = 350  # Adjust the width as needed

    wn.fill((255, 255, 255))  # Fill background with white
    pygame.draw.rect(wn, river_color, (300 - river_width // 2, 0, river_width, 600))  # Draw the vertical river in the center

    pygame.display.update()
