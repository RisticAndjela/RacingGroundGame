import pygame
import sys

def chose_level():
    # Initialize Pygame
    pygame.init()

    # Set up window
    width, height = 400, 200
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Enter Level")

    # Set up colors
    white = (255, 255, 255)
    black = (0, 0, 0)

    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up input box
    input_box = pygame.Rect(50, 90, 300, 36)

    text = ''
    active = False

    # Set up prompt text
    prompt_text = font.render("Chose Level difficulty from 1-3:", True, black)

    # Set up game loop
    clock = pygame.time.Clock()
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return text 
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        window.fill(white)

        # Draw prompt text
        window.blit(prompt_text, (10, 50))

        # Draw input box
        txt_surface = font.render(text, True, (0,0,255))
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        window.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.draw.rect(window, (0,0,255), input_box, 2)

        pygame.display.flip()
        clock.tick(30)

