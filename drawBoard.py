import pygame


wking = pygame.image.load('./assets/Chess_klt60.png')
wqueen = pygame.image.load('./assets/Chess_qlt60.png')
wbishop = pygame.image.load('./assets/Chess_blt60.png')
wknight = pygame.image.load('./assets/Chess_nlt60.png')
wrook = pygame.image.load('./assets/Chess_kdl45.png')
wpawn = pygame.image.load('./assets/Chess_plt60.png')

bking = pygame.image.load('./assets/Chess_kdt60.png')
bqueen = pygame.image.load('./assets/Chess_qdt60b.png')
bbishop = pygame.image.load('./assets/Chess_bdt60.png')
bknight = pygame.image.load('./assets/Chess_ndt60.png')
brook = pygame.image.load('./assets/Chess_rdt60.png')
bpawn = pygame.image.load('./assets/Chess_pdt60.png')

board = []


def drawWhiteBoard(screen, BLACK, WHITE):
    pygame.display.set_caption('Play Chess!')
    # Assume 'screen' is your display Surface object
    screen.fill((0, 0, 0))  # This will fill the entire screen with black color
    # Update the full display Surface to the screen

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

    updateBoard(screen)

    
        

def drawBlackBoard(screen, BLACK, WHITE):
    pygame.display.set_caption('Play Chess!')
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


def makeBoardB():
    board.append([[wrook, 5], [wknight, 3], [wbishop, 3], [wking, float('inf')], [wqueen, 9], [wbishop, 3], [wknight, 3], [wrook, 5]])
    board.append([[wpawn, 1], [wpawn, 1], [wpawn, 1], [wpawn, 1], [wpawn, 1], [wpawn, 1], [wpawn, 1], [wpawn, 1]])
    for y in range(4):
        board.append([[None], [None], [None], [None], [None], [None], [None], [None]])


    board.append([[bpawn, 1], [bpawn, 1], [bpawn, 1], [bpawn, 1], [bpawn, 1], [bpawn, 1], [bpawn, 1], [bpawn, 1]])
    board.append([[brook, 5], [bknight, 3], [bbishop, 3], [bking, float('inf')], [bqueen, 9], [bbishop, 3], [bknight, 3], [brook, 5]])


def makeBoardW():
    board.append([[brook, 5, "r", [0, 0], "b"], [bknight, 3, "n", [0, 1], "b"], [bbishop, 3, "b", [0, 2], "b"], [bking, float('inf'), "k", [0, 3], "b"], [bqueen, 9, "q", [0, 4], "b"], [bbishop, 3, "b", [0, 5], "b"], [bknight, 3, "n", [0, 6], "b"], [brook, 5, "r", [0, 7], "b"]])
    board.append([[bpawn, 1, "p", [1, 0], "b"], [bpawn, 1, "p", [1, 1], "b"], [bpawn, 1, "p", [1, 2], "b"], [bpawn, 1, "p", [1, 3], "b"], [bpawn, 1, "p", [1, 4], "b"], [bpawn, 1, "p", [1, 5], "b"], [bpawn, 1, "p", [1, 6], "b"], [bpawn, 1, "p", [1, 7], "b"]])
    for y in range(4):
        board.append([[None], [None], [None], [None], [None], [None], [None], [None]])

    board.append([[wpawn, 1, "p", [6, 0], "w"], [wpawn, 1, "p", [6, 1], "w"], [wpawn, 1, "p", [6, 2], "w"], [wpawn, 1, "p", [6, 3], "w"], [wpawn, 1, "p", [6, 4], "w"], [wpawn, 1, "p", [6, 5], "w"], [wpawn, 1, "p", [6, 6], "w"], [wpawn, 1, "p", [6, 7], "w"]])
    board.append([[wrook, 5, "r", [7, 0], "w"], [wknight, 3, "n", [7, 1], "w"], [wbishop, 3, "b", [7, 2], "w"], [wking, float('inf'), "k", [7, 3], "w"], [wqueen, 9, "q", [7, 4], "w"], [wbishop, 3, "b", [7, 5], "w"], [wknight, 3, "n", [7, 6], "w"], [wrook, 5, "r", [7, 7], "w"]])

def updateBoard(screen):
    h = 0
    w = 0
    for y in board:
        w = 0
        for x in y:
            if x[0] != None:
                screen.blit(x[0], (w*100, h*100))
            w += 1
        h +=1

    pygame.display.flip()



def legalMovesWhite(piece):
    squares = []
    if piece[0] != None and piece[4] == "w":

        if piece[2] == "p":

            if piece[3][0] == 6:
                if board[piece[3][0]-1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-1, piece[3][1]])
                if board[piece[3][0]-2][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-2, piece[3][1]])


            if (piece[3][0]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]][0] == None:
                    squares.append([piece[3][0]-1, piece[3][1]])

            
            if (piece[3][0]-1 >= 0 and piece[3][1]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]-1][0] is not None and board[piece[3][0]-1][piece[3][1]-1][4] == "b":
                    squares.append([piece[3][0]-1, piece[3][1]-1])

            if (piece[3][0]-1 >= 0 and piece[3][1]+1 < 8):
                if board[piece[3][0]-1][piece[3][1]+1][0] is not None and board[piece[3][0]-1][piece[3][1]+1][4] == "b":
                    squares.append([piece[3][0]-1, piece[3][1]+1])

        if piece[2] == 'n':
            if (piece[3][0]-2 >= 0 and piece[3][1]-1 >= 0):
                if (board[piece[3][0]-2][piece[3][1]-1][0] == None or board[piece[3][0]-2][piece[3][1]-1][4] == "b"):
                    squares.append([piece[3][0]-2, piece[3][1]-1])

            if (piece[3][0]-2 >= 0 and piece[3][1]+1 < 8):
                if (board[piece[3][0]-2][piece[3][1]+1][0] == None or board[piece[3][0]-2][piece[3][1]+1][4] == "b"):
                    squares.append([piece[3][0]-2, piece[3][1]+1])

            if (piece[3][0]-1 >= 0 and piece[3][1]-2 >= 0):
                if (board[piece[3][0]-1][piece[3][1]-2][0] == None or board[piece[3][0]-1][piece[3][1]-2][4] == "b"):
                    squares.append([piece[3][0]-1, piece[3][1]-2])

            if (piece[3][0]-1 >= 0 and piece[3][1]+2 < 8):
                if (board[piece[3][0]-1][piece[3][1]+2][0] == None or board[piece[3][0]-1][piece[3][1]+2][4] == "b"):
                    squares.append([piece[3][0]-1, piece[3][1]+2])

            if (piece[3][0]+1 < 8 and piece[3][1]+2 < 8):
                if (board[piece[3][0]+1][piece[3][1]+2][0] == None or board[piece[3][0]+1][piece[3][1]+2][4] == "b"):
                    squares.append([piece[3][0]+1, piece[3][1]+2])
            
            if (piece[3][0]+1 < 8 and piece[3][1]-2 >= 0):
                if (board[piece[3][0]+1][piece[3][1]-2][0] == None or board[piece[3][0]+1][piece[3][1]-2][4] == "b"):
                    squares.append([piece[3][0]+1, piece[3][1]-2])
            
            if (piece[3][0]+2 < 8 and piece[3][1]+1 < 8):
                if (board[piece[3][0]+2][piece[3][1]+1][0] == None or board[piece[3][0]+2][piece[3][1]+1][4] == "b"):
                    squares.append([piece[3][0]+2, piece[3][1]+1])

            if (piece[3][0]+2 < 8 and piece[3][1]-1 >= 0):
                if (board[piece[3][0]+2][piece[3][1]-1][0] == None or board[piece[3][0]+2][piece[3][1]-1][4] == "b"):
                    squares.append([piece[3][0]+2, piece[3][1]-1])

        if piece[2] == 'k':
            if (piece[3][0]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]][0] == None or board[piece[3][0]-1][piece[3][1]][4] == 'b':
                    squares.append([piece[3][0]-1, piece[3][1]])

            if (piece[3][0]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]][0] == None or board[piece[3][0]+1][piece[3][1]][4] == 'b':
                    squares.append([piece[3][0]+1, piece[3][1]])

            if (piece[3][1]-1 >= 0):
                if board[piece[3][0]][piece[3][1]-1][0] == None or board[piece[3][0]][piece[3][1]-1][4] == 'b':
                    squares.append([piece[3][0], piece[3][1]-1])

            if (piece[3][1]+1 < 8):
                if board[piece[3][0]][piece[3][1]+1][0] == None or board[piece[3][0]][piece[3][1]+1][4] == 'b':
                    squares.append([piece[3][0], piece[3][1]+1])
                
            if (piece[3][0]+1 < 8 and piece[3][1]+1 < 8):
                if board[piece[3][0]+1][piece[3][1]+1][0] == None or board[piece[3][0]+1][piece[3][1]+1][4] == 'b':
                    squares.append([piece[3][0]+1, piece[3][1]+1])
                
            if (piece[3][0]+1 < 8 and piece[3][1]-1 >= 0):
                if board[piece[3][0]+1][piece[3][1]-1][0] == None or board[piece[3][0]+1][piece[3][1]-1][4] == 'b':
                    squares.append([piece[3][0]+1, piece[3][1]-1])

            if (piece[3][0]-1 >= 0 and piece[3][1]+1 < 8):
                if board[piece[3][0]-1][piece[3][1]+1][0] == None or board[piece[3][0]-1][piece[3][1]+1][4] == 'b':
                    squares.append([piece[3][0]-1, piece[3][1]+1])
                
            if (piece[3][0]-1 >= 0 and piece[3][1]-1 >= 0):
                if board[piece[3][0]-1][piece[3][1]-1][0] == None or board[piece[3][0]-1][piece[3][1]-1][4] == 'b':
                    squares.append([piece[3][0]-1, piece[3][1]-1])

        if piece[2] == 'b':
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                    elif board[piece[3][0]-v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]+v < 8):
                    if board[piece[3][0]-v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                    elif board[piece[3][0]-v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                    elif board[piece[3][0]+v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]-v >= 0):
                    if board[piece[3][0]+v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                    elif board[piece[3][0]+v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

        if piece[2] == 'r':
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]])
                    elif board[piece[3][0]-v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]+v < 8):
                    if board[piece[3][0]][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0], piece[3][1]+v])
                    elif board[piece[3][0]][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]])
                    elif board[piece[3][0]+v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]-v >= 0):
                    if board[piece[3][0]][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0], piece[3][1]-v])
                    elif board[piece[3][0]][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

        if piece[2] == 'q':

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]])
                    elif board[piece[3][0]-v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]+v < 8):
                    if board[piece[3][0]][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0], piece[3][1]+v])
                    elif board[piece[3][0]][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]])
                    elif board[piece[3][0]+v][piece[3][1]][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][1]-v >= 0):
                    if board[piece[3][0]][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0], piece[3][1]-v])
                    elif board[piece[3][0]][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0], piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False
            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]-v >= 0):
                    if board[piece[3][0]-v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                    elif board[piece[3][0]-v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]-v >= 0 and piece[3][1]+v < 8):
                    if board[piece[3][0]-v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                    elif board[piece[3][0]-v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]-v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]+v < 8):
                    if board[piece[3][0]+v][piece[3][1]+v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                    elif board[piece[3][0]+v][piece[3][1]+v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]+v])
                        di = False
                    else:
                        di = False
                else:
                    di = False


            di = True
            v = 0
            while di:
                v += 1
                if (piece[3][0]+v < 8 and piece[3][1]-v >= 0):
                    if board[piece[3][0]+v][piece[3][1]-v][0] == None:
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                    elif board[piece[3][0]+v][piece[3][1]-v][4] == 'b':
                        squares.append([piece[3][0]+v, piece[3][1]-v])
                        di = False
                    else:
                        di = False
                else:
                    di = False

                    




    print(squares)
    return squares

def returnPiece(x, y):
    return board[y][x]

def drawMoves(screen, squares):

    if len(squares) != 0:

        RED = (255, 0, 0)
        # Create a new Surface with the size of the rectangle you want to draw
        rect_surface = pygame.Surface((100, 100))

        # Fill the new Surface with the color you want (here, WHITE)
        rect_surface.fill(RED)

        # Set the alpha value of the Surface (0 is fully transparent, 255 is opaque)
        rect_surface.set_alpha(128)  # Semi-transparent

        for x in squares:
            screen.blit(rect_surface, (x[1]*100, x[0]*100))

    pygame.display.flip()

def playerMoved(index, piece):
    if index[0] == 0 and piece[2] == "p":
        piece[0] = wqueen
        piece[1] = 9
        piece[2] = 'q'

    current_piece = piece[3]
    board[current_piece[0]][current_piece[1]] = [None]
    piece[3] = index
    board[index[0]][index[1]] = piece
    print(board)
