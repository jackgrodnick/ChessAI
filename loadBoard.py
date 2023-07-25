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

players_turn = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

moves = []
selected_piece = None

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos  # gets mouse position

            if human_color is None:
                human_color = chooseColor.getPlayerColor(mouse_pos)
                if human_color == "White":
                    drawBoard.makeBoardW()
                    drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                    players_turn = True

                elif human_color == "Black":
                    drawBoard.makeBoardB()
                    drawBoard.drawBlackBoard(screen, BLACK, WHITE)

            if len(moves) != 0 and selected_piece is not None:
                if [mouse_pos[1]//100, mouse_pos[0]//100] in moves:
                    print('d')
                    drawBoard.playerMoved([mouse_pos[1]//100, mouse_pos[0]//100], selected_piece)
                    if human_color == "White":
                        drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                    elif human_color == "Black":
                        drawBoard.drawBlackBoard(screen, BLACK, WHITE) 

            if players_turn:

                temp = drawBoard.returnPiece(mouse_pos[0]//100, mouse_pos[1]//100)

                if temp == selected_piece:
                    if human_color == "White":
                        drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                        selected_piece = None
                        continue
                    elif human_color == "Black":
                        drawBoard.drawBlackBoard(screen, BLACK, WHITE)
                        selected_piece = None
                        continue
                else:
                    if human_color == "White":
                        drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                    elif human_color == "Black":
                        drawBoard.drawBlackBoard(screen, BLACK, WHITE)
            
                selected_piece = temp

                print(mouse_pos[0]//100, mouse_pos[1]//100)

                print(selected_piece)

                moves = drawBoard.legalMovesWhite(selected_piece)

                drawBoard.drawMoves(screen, moves)
       

        
    if human_color is None:
        chooseColor.drawMain(screen, canvas_width, canvas_height)
        

# Quit pygame
pygame.quit()