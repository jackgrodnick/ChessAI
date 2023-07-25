import pygame
import chooseColor
import drawBoard

pygame.init()

canvas_width = 800
canvas_height = 800

screen = pygame.display.set_mode((canvas_width, canvas_height))

running = True

ai_color = None
human_color = None

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  # gets mouse position

            if human_color is None:
                human_color = chooseColor.getPlayerColor(mouse_pos)
                if human_color == "White":
                    drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                elif human_color == "Black":
                    drawBoard.drawWhiteBoard(screen, BLACK, WHITE)

        
    if human_color is None:
        chooseColor.drawMain(screen, canvas_width, canvas_height)
        

# Quit pygame
pygame.quit()