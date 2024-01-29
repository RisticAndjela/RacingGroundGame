import pygame
import sys

def send_message(message):
    pygame.init()
    # Set up window
    width, height = 400, 200
    window = pygame.display.set_mode((width, height))
    
    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up prompt text
    prompt_text = font.render(message, True, black)

    # Set up game loop
    clock = pygame.time.Clock()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
        window.fill(white)

        # Draw prompt text
        window.blit(prompt_text, (10, 50))

        pygame.display.flip()
        clock.tick(30)

