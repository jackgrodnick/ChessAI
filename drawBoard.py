import pygame

def drawWhiteBoard(screen, BLACK, WHITE):
    # Assume 'screen' is your display Surface object
    screen.fill((0, 0, 0))  # This will fill the entire screen with black color
    # Update the full display Surface to the screen
    pygame.display.flip()

    square_color = WHITE
    for y in range(8):
        if (y+1) % 2 == 0:
            square_color = BLACK
        else:
            square_color = WHITE
        for x in range(8):
            pygame.draw.rect(screen, square_color, (x*100, y*100, 100, 100))
            if square_color == BLACK:
                square_color = WHITE
            else:
                square_color = BLACK

    pygame.display.flip()
        

def drawBlackBoard(screen, BLACK, WHITE):
    # Assume 'screen' is your display Surface object
    screen.fill((0, 0, 0))  # This will fill the entire screen with black color
    # Update the full display Surface to the screen
    pygame.display.flip()

    square_color = WHITE
    for y in range(8):

        if (y+1) % 2 == 0:
            square_color = BLACK
        else:
            square_color = WHITE

        for x in range(8):

            pygame.draw.rect(screen, square_color, (x*100, y*100, 100, 100))

            if square_color == BLACK:
                square_color = WHITE
            else:
                square_color = BLACK
                
    pygame.display.flip()
    