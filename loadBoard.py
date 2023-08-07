import pygame
import chooseColor
import drawBoard
import chessAI

pygame.init()

canvas_width = 800
canvas_height = 800

screen = pygame.display.set_mode((canvas_width, canvas_height))

running = True

ai_color = None
human_color = None

players_turn = False

WHITE = (255, 255, 255)
BLACK = (211, 211, 211)

moves = []
selected_piece = None

def display_winner(winner):
    font = pygame.font.SysFont(None, 55)
    if winner == "Black":
        text = font.render('Black Won!', True, (0, 0, 0), (255, 255, 255))
    else:
        text = font.render('White Won!', True, (255, 255, 255), (0, 0, 0))
    
    text_rect = text.get_rect(center=(canvas_width/2, canvas_height/2))
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                return
        
        screen.fill((255, 255, 255))
        screen.blit(text, text_rect)
        pygame.display.flip()
    


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos = event.pos  # gets mouse position

            if human_color is None:
                human_color = chooseColor.getPlayerColor(mouse_pos)

                if human_color == "White":
                    ai_color = "Black"
                elif human_color == "Black":
                    ai_color = "White"

                if human_color == "White":
                    drawBoard.makeBoard()
                    drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                    players_turn = True

                elif human_color == "Black":
                    drawBoard.makeBoard()
                    drawBoard.drawBlackBoard(screen, BLACK, WHITE)
                    players_turn = False


            if players_turn:
                print("attack: ", drawBoard.findAttackers(drawBoard.getBoard()))

                if len(moves) != 0 and selected_piece is not None:
                    if [mouse_pos[1]//100, mouse_pos[0]//100] in moves:
                        drawBoard.playerMoved([mouse_pos[1]//100, mouse_pos[0]//100], selected_piece)
                        players_turn = False
                        if human_color == "White":
                            drawBoard.drawWhiteBoard(screen, BLACK, WHITE)
                        elif human_color == "Black":
                            drawBoard.drawBlackBoard(screen, BLACK, WHITE)

                        temp = None
                        selected_piece = None
                        moves = []
                        continue

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

                if human_color == "White":
                    # moves = drawBoard.legalMovesWhite(selected_piece, "front")
                    moves = drawBoard.legalMoves(selected_piece)

                    if moves == "Black Won!":
                        display_winner("Black")
                        running = False  # End the main loop

                    
                elif human_color == "Black":
                    # moves = drawBoard.legalMovesBlack(selected_piece, "front")
                    moves = drawBoard.legalMoves(selected_piece)
                    if moves == "White Won!":
                        display_winner("White")
                        running = False  # End the main loop
                    

                drawBoard.drawMoves(screen, moves)
            

    if not players_turn and human_color is not None:
        result = chessAI.move(drawBoard.getBoard(), ai_color, screen, BLACK, WHITE)
        if result is not None:
            display_winner(result)
        players_turn = True
       

        
    if human_color is None:
        chooseColor.drawMain(screen, canvas_width, canvas_height)

# Quit pygame
pygame.quit()