
import pygame


button_width = 200
button_height = 100

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)

white_button_position = None
black_button_position = None


def drawMain(screen, canvas_width, canvas_height):
    pygame.display.set_caption('Choose your Color')
    global white_button_position, black_button_position

    white_button_position = (canvas_width//2 - button_width - 50, canvas_height//2)
    black_button_position = (canvas_width//2 + 50, canvas_height//2)

    # Create font object once and render text into surfaces
    font = pygame.font.Font(None, 32)  # None for the default font
    white_text = font.render('White', True, BLACK)  # Black color
    black_text = font.render('Black', True, WHITE)  # White color
    caption_text = font.render('Choose your Color', True, BLACK)


    #Fill the background with a light gray color
    screen.fill(LIGHT_GRAY)

    screen.blit(caption_text, ((canvas_width//2) - 100, (canvas_height//2)-200))

    # Draw the white button
    pygame.draw.rect(screen, WHITE, pygame.Rect(white_button_position[0], white_button_position[1], button_width, button_height))
    screen.blit(white_text, (white_button_position[0] + 50, white_button_position[1] + 35))  # Adjust these values as you see fit

    # Draw the black button
    pygame.draw.rect(screen, BLACK, pygame.Rect(black_button_position[0], black_button_position[1], button_width, button_height))
    screen.blit(black_text, (black_button_position[0] + 60, black_button_position[1] + 35))  # Adjust these values as you see fit


    # Update the full display surface to the screen
    pygame.display.flip()


def getPlayerColor(mouse_pos):

    # check if mouse position is over the white button
    if white_button_position[0] <= mouse_pos[0] <= white_button_position[0] + button_width and \
        white_button_position[1] <= mouse_pos[1] <= white_button_position[1] + button_height:
        print("Human is white player")
        return "White"

    # check if mouse position is over the black button
    elif black_button_position[0] <= mouse_pos[0] <= black_button_position[0] + button_width and \
        black_button_position[1] <= mouse_pos[1] <= black_button_position[1] + button_height:
        print("Human is black player")
        return "Black"